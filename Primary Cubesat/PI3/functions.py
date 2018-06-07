from time import sleep
import serial
import minimalmodbus as mini

class Clock:
    def __init__(self):
        self.second = 0
        self.minute = 0

    def increment(self, t):
        while 1:
            self.second+=1
            if self.second == 60:
                self.minute+=1
                self.second = 0
            t[0] = self.minute
            t[1] = self.second
            sleep(1)

class Laser:
    def __init__(self, port):
        mini.BAUDRATE=115200
        self.primaryInstrument = mini.Instrument("/dev/ttyUSB1", 1, mode='rtu')
        self.primaryInstrument.write_register(4, value=20, functioncode=6)

    def measure(self, conn, t):
        while 1:
            primaryPass = self.primaryInstrument.read_register(24, functioncode = 4)
            instance = None

            if primaryPass is not 0:
                instance = ("Laser passed at " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + " at a distance of " + str(primaryPass).zfill(3) + ".") #43 bytes

            if instance is not None:
                with open("masterLog.txt", "a+") as f:
                    f.write(instance+"\n")
                conn.send(instance)

class Iridium:
    def __init__(self, port):
        self.ser = serial.Serial(port="/dev/ttyUSB0", baudrate=19200, xonxoff=True)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    def broadcast(self):
        byteMessage =
        while True:
            self.ser.write(b'\x41\x54\x2b\x53\x42\x44\x57\x52\x54\x3d\x49\x27\x6d\x20\x61\x6c\x69\x76\x65\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d') #31 Bytes
            sleep(.1)
            self.ser.write('AT+SBDIX\r'.encode())
            self.ser.flush()

    def sendMessage(self, m):
        returned = None
        self.ser.write(('AT+SBDWRT= ' + m + '\r').encode())
        sleep(.1)
        self.ser.reset_input_buffer()
        self.ser.write('AT+SBDIX\r'.encode())
        sleep(.1)
        strip = str.maketrans( '', '', '\r\n,')
        returned = self.ser.read(size=self.ser.in_waiting).decode().translate(strip).split(" ")
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

        if returned is not None:
            if len(returned) > 1:
                if returned[0] == '+SBDIX:':
                    if returned[1] != '0':
                        self.sendMessage(m)
