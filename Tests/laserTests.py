import minimalmodbus as mini
from time import sleep
import serial

class Laser:
    def __init__(self):
        mini.BAUDRATE=115200
        try:
            self.primaryInstrument = mini.Instrument("/dev/ttyUSB0", 1, mode='rtu')
        except:
            self.primaryInstrument = mini.Instrument("/dev/ttyUSB1", 1, mode='rtu')
        self.primaryInstrument.write_register(4, value=20, functioncode=6)

    def measure(self, conn):
        primaryPass = self.primaryInstrument.read_register(24, functioncode = 4)
        instance = None

        if primaryPass is not 0:
            instance = ("Laser passed at " + str(primaryPass))

        if instance is not None:
            conn.send(instance)

class Iridium:
    def __init__(self):
        try:
            self.ser = serial.Serial(port="/dev/ttyUSB1", baudrate=19200, xonxoff=True)
        except:
            self.ser = serial.Serial(port="/dev/ttyUSB0", baudrate=19200, xonxoff=True)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    def sendMessage(self, m):
        returned = None
        self.ser.write(('AT+SBDWRT= ' + m + '\r').encode())
        sleep(.1)
        self.ser.reset_input_buffer()
        self.ser.write('AT+SBDIX\r'.encode())
        sleep(.1)
        print(self.ser.read(size=self.ser.in_waiting).decode())
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
