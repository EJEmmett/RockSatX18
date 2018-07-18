from time import sleep
from io import BytesIO
import serial
import minimalmodbus as mini
import picamera

def clock(t):
    second = 0
    minute = 0
    while 1:
        second += 1
        if second == 60:
            minute += 1
            second = 0
        t[0] = minute
        t[1] = second
        sleep(1)

class Laser:
    def __init__(self):
        mini.BAUDRATE = 115200
        try:
            self.primary_instrument = mini.Instrument("/dev/ttyUSB0", 1, mode='rtu')
        except:
            self.primary_instrument = mini.Instrument("/dev/ttyUSB1", 1, mode='rtu')
        self.primary_instrument.write_register(4, value=20, functioncode=6)

    def measure(self, laser_c, t):
        while 1:
            primary_pass = self.primary_instrument.read_register(24, functioncode=4)
            instance = None

            if primary_pass is not 0:
                instance = primary_pass

            if instance is None:
                laser_c.send("Laser passed at " + str(t[0]).zfill(2) + ":" + str(t[1]).zfill(2) + "          ")#31 Bytes

class Iridium:
    def __init__(self):
        try:
            self.ser = serial.Serial(port="/dev/ttyUSB1", baudrate=19200, xonxoff=True)
        except:
            self.ser = serial.Serial(port="/dev/ttyUSB0", baudrate=19200, xonxoff=True)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    def image_transmission(self, stream_p):
        split_stream = list(stream_p.recv_bytes())
        self.ser.write(b'AT+SBDWT=[Start]')
        sleep(.1)
        self.ser.write(b'AT+SBDIX\r')
        sleep(.1)
        self.ser.write(b'AT+SBDD0\r')

        while split_stream:
            self.ser.write(("AT+SBDWT=[" + str(bytes(split_stream[0:118])) + "]\r").encode())
            sleep(.1)
            self.ser.write(b'AT+SBDIX\r')
            sleep(.1)
            self.ser.write(b'AT+SBDD0\r')
            del split_stream[0:118]

        self.ser.write(b'AT+SBDWT=[Stop]')
        sleep(.1)
        self.ser.write(b'AT+SBDIX\r')
        sleep(.1)
        self.ser.write(b'AT+SBDD0\r')

    def register(self):
        while True:
            self.ser.write(b'AT+SBDREG')
            sleep(.1)

    def broadcast(self):
        while True:
            self.ser.write(b'AT+SBDWT=(Hello World                    )\r') #31 Bytes
            sleep(.1)
            self.ser.write(b'AT+SBDIX\r')
            sleep(.1)
            self.ser.write(b'AT+SBDD0\r')

    def send_message(self, laser_p):
        self.ser.write(('AT+SBDWRT=(' + laser_p.recv() + ')\r').encode())
        sleep(.1)
        self.ser.write(b'AT+SBDIX\r')
        sleep(.1)
        self.ser.write(b'AT+SBDD0\r')

def capture_picture(stream_c):
    camera = picamera.PiCamera()
    camera.exposure_mode = 'antishake'
    camera.resolution = (1025, 768)

    sleep(2)
    index = 0
    maximum = 135

    for x in range(3):
        file = open('image.jpg', 'wb')
        camera.capture(file, resize=(38, 38))
        file.close()

        file = open('image.jpg', 'rb')
        stream_c.send_bytes(file.read())
        file.close()

    while index < maximum:
        camera.capture("/home/pi/Pictures/pic" + str(index + 1) + ".png")
        index += 1
        sleep(5)
