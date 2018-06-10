import minimalmodbus as mini
from pygame import mixer
import picamera
import serial
from time import sleep

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
    def __init__(self):
        mini.BAUDRATE=115200
        try:
            self.primaryInstrument = mini.Instrument("/dev/ttyUSB0", 1, mode='rtu')
        except:
            self.primaryInstrument = mini.Instrument("/dev/ttyUSB1", 1, mode='rtu')
        self.primaryInstrument.write_register(4, value=20, functioncode=6)

    def measure(self):
        print("Laser start")
        while 1:
            primaryPass = self.primaryInstrument.read_register(24, functioncode = 4)
            instance = None

            if primaryPass is not 0:
                instance = ("Laser passed at " + str(primaryPass))

            if instance is not None:
                print(instance)
                sleep(5)

class Iridium:
    def __init__(self):
        try:
            self.ser = serial.Serial(port="/dev/ttyUSB1", baudrate=19200, xonxoff=True)
        except:
            self.ser = serial.Serial(port="/dev/ttyUSB0", baudrate=19200, xonxoff=True)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    def broadcast(self):
        print("Broadcast Start")
        while True:
            self.ser.write(b'\x41\x54\x2b\x53\x42\x44\x57\x52\x54\x3d\x49\x27\x6d\x20\x61\x6c\x69\x76\x65\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d') #31 Bytes
            sleep(.1)
            self.ser.write('AT+SBDIX\r'.encode())
            sleep(.1)
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
            print("Broadcast still going")

    def sendMessage(self, m):
        returned = None
        self.ser.write(('AT+SBDWRT= ' + m + '\r').encode())
        sleep(.1)
        self.ser.reset_input_buffer()
        self.ser.write('AT+SBDIX\r'.encode())
        sleep(.1)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

class Cam:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.exposure_mode = 'antishake'

    def cap(self):
        print("Camera Starting")
        #sleep(79)
        outputVersion = 1
        index = 0
        max = 135

        while(index < max):
            print(outputVersion)
            self.camera.capture("/home/pi/Pictures/pic" + str(outputVersion) + ".png")
            index += 1
            outputVersion += 1
            sleep(5)

class Music:
    def __init__(self):
        self.file1 = '/home/pi/Music/danger_zone.mp3'
        self.file2 = '/home/pi/Music/Starman.mp3'
        self.file3 = '/home/pi/Music/cakes.mp3'
        self.file4 = '/home/pi/Music/space_oddity.mp3'
        self.file5 = '/home/pi/Music/staying_alive.mp3'

    def begin(self):
        print("Music Start")
        mixer.init()
        sleep(0.1)
        mixer.music.load(self.file1)
        mixer.music.play()
        sleep(180)

        mixer.music.load(self.file2)
        mixer.music.play()
        sleep(180)

        mixer.music.load(self.file3)#the ONE rap song...
        mixer.music.play()
        sleep(180)

        mixer.music.load(self.file4)
        mixer.music.play()
        sleep(180)

        mixer.music.load(self.file5)
        mixer.music.play()
        sleep(180)

        mixer.stop()
        print("Music Stop")
