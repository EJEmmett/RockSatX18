from time import sleep
from datetime import datetime
import minimalmodbus as mini
import serial

class Laser(object):
    def __init__(self):
        mini.BAUDRATE=115200
        self.primaryInstrument = mini.Instrument("/dev/ttyUSB0",1,mode='rtu')
        self.secondaryInstrument = mini.Instrument("/dev/ttyUSB1",2,mode='rtu')

    def measure(self):
        primaryPass = self.primaryInstrument.read_register(24, functioncode = 4)
        secondaryPass = self.secondaryInstrument.read_register(24, functioncode = 4)
        instance = None

        if primaryPass < 1000:
            instance = ('Laser 1 passed at: {}'.format(datetime.now().strftime('%H:%M:%S')))
        if secondaryPass < 1000:
            instance = ('Laser 2 was passed at: {}'.format(datetime.now().strftime('%H:%M:%S')))

        if instance is not None:
            with open("Lasers.txt", "a") as f:
                f.write(instance+"\n")
            q.put(instance)

class Iridium(object):
    def __init__(self):
        self.ser = serial.Serial(port='/dev/ttyUSB2', baudrate=19200, xonxoff=True)

    def broadcast(self):
        self.ser.write('AT+SBDIX\r'.encode())
        sleep(.5)

    def sendMessage(self, m):
        self.ser.write('AT+SDBWT={}\r'.format(m).encode())
        sleep(1)
        self.ser.write('AT+SBDIX\r'.encode())
        returned = self.ser.read(self.ser.in_waiting).strip().split('\n')

        if(isinstance(returned, list) and len(returned)>1):
            if(len(returned)>2):
                if(returned[1] is not '0'):
                    self.sendMessage(m)
                else:
                    pass
            else:
                self.sendMessage(m)
        else:
            self.sendMessage(m)

        return returned
