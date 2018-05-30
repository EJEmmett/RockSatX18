from time import sleep
import serial
from datetime import datetime
import minimalmodbus as mini

#def failsafe(q):
#    q.put()


class Laser:
    def __init__(self, port):
        mini.BAUDRATE=115200
        self.primaryInstrument = mini.Instrument(port, 1, mode='rtu')
        self.primaryInstrument.write_register(4, value=20, functioncode=6)

    def measure(self,q):
        primaryPass = self.primaryInstrument.read_register(24, functioncode = 4)
        instance = None

        if primaryPass is not 0:
            instance = ('Laser passed at: ' + datetime.now().strftime('%H:%M:%S'))

        if instance is not None:
            with open("Laser.txt", "a") as f:
                f.write(instance+"\n")
            q.put(instance)

class Iridium:
    def __init__(self, port):
        self.ser = serial.Serial(port=port, baudrate=19200, xonxoff=True)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    def broadcast(self):
        while True:
            self.ser.write('AT+SBDWRT=I\'m alive'.encode())
            sleep(.1)
            self.ser.write('AT+SBDIX\r'.encode())
            self.ser.flush()

    def sendMessage(self, m):
        self.ser.write(('AT+SBDWRT= ' + m + '\r').encode())
        sleep(.1)
        self.ser.reset_input_buffer()
        self.ser.write('AT+SBDIX\r'.encode())
        strip = str.maketrans( '', '', '\r\n,')
        returned = self.ser.read(size=self.ser.in_waiting).decode().translate(strip).split(" ")
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

        if returned is not None:
            if len(returned) > 1:
                if returned[0] == '+SBDIX:':
                    if returned[1] != '0':
                        self.sendMessage(m)
