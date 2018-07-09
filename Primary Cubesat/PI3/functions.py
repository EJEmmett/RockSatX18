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
        while True:
            self.ser.write(("AT+SBDWT=" + bytes(split_stream[0:120]) + "\r").encode())
            sleep(.1)
            self.ser.write(b'AT+SBDIX\r')
            sleep(.1)
            self.ser.write(b'AT+SBDD0\r')
            del split_stream[0:120]

    def broadcast(self):
        while True:
            self.ser.write(b'AT+SBDWT=Hello World                    \r') #31 Bytes
            sleep(.1)
            self.ser.write(b'AT+SBDIX\r')
            sleep(.1)
            self.ser.write(b'AT+SBDD0\r')

    def send_message(self, message):
        self.ser.write(('AT+SBDWRT=' + message + '\r').encode())
        sleep(.1)
        self.ser.write(b'AT+SBDIX\r')
        sleep(.1)
        self.ser.write(b'AT+SBDD0\r')

def capture_picture(stream_c):
    camera = picamera.PiCamera()
    camera.exposure_mode = 'antishake'

    sleep(2)
    index = 0
    maximum = 135

    photo_stream = BytesIO()
    camera.capture(photo_stream, 'jpeg', resize=(38, 38))
    stream_c.send(photo_stream.read())

    while index < maximum:
        camera.capture("/home/pi/Pictures/pic" + str(index + 1) + ".png")
        index += 1
        sleep(5)
