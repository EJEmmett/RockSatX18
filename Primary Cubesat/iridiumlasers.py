from time import sleep
from datetime import datetime
import minimalmodbus as mini
import serial

class Iridium(object):
    def __init__(self):
        self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=19200, xonxoff=True)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    def broadcast(self):
        self.ser.write('AT+SBDWRT=I\'m alive'.encode())
        sleep(.1)
        self.ser.write('AT+SBDIX\r'.encode())
        self.ser.flush()

    def sendMessage(self, m):
        self.ser.write('AT+SBDWRT={}\r'.format(m).encode())
        sleep(.1)
        self.ser.reset_input_buffer()
        self.ser.write('AT+SBDIX\r'.encode())
        strip = str.maketrans( '', '', '\r\n,')
        returned = self.ser.read(size=self.ser.in_waiting).decode().translate(strip).split(" ")
        self.ser.flush()

        if returned is not None:
            if len(returned) > 1:
                if returned[0] == '+SBDIX:':
                    if returned[1] != '0':
                        self.sendMessage(m)

class Laser(object):
    def __init__(self):
        mini.BAUDRATE=115200
        self.primaryInstrument = mini.Instrument("/dev/ttyUSB1", 1, mode='rtu')
        self.secondaryInstrument = mini.Instrument("/dev/ttyUSB2", 2, mode='rtu')

    def measure(self,q):
        primaryPass = self.primaryInstrument.read_register(24, functioncode = 4)
        secondaryPass = self.secondaryInstrument.read_register(24, functioncode = 4)
        instance = None

        if primaryPass is not 0:
            instance = ('Laser 1 passed at: {}'.format(datetime.now().strftime('%H:%M:%S')))
        if secondaryPass is not 0:
            instance = ('Laser 2 was passed at: {}'.format(datetime.now().strftime('%H:%M:%S')))

        if instance is not None:
            with open("Lasers.txt", "a") as f:
                f.write(instance+"\n")
            q.put(instance)
