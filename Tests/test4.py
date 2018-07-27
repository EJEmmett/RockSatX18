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
                laser_c.send("Laser passed at " + str(t[0]).zfill(2) + ":" + str(t[1]).zfill(2) + "          ")#31 Bytesw       

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
        maxBytes = len(split_stream)
        #array = [ 1 , 2, 3, 4, 5, 6, 7]
        im = [1, 2, 3, 4, 5, 6, 7]
        print("split stream 1:" +  str(split_stream[0:1])) 
        split_stream1 = ''.join(map(str, split_stream[0:150]))
        split_stream2 = ''.join(map(str, split_stream[150:300]))
        split_stream3 = ''.join(map(str, split_stream[300:450]))
        split_stream4 = ''.join(map(str, split_stream[450:600]))
        split_stream5 = ''.join(map(str, split_stream[750:900]))
        split_stream6 = ''.join(map(str, split_stream[900:1500]))
        split_stream7 = ''.join(map(str, split_stream[:maxBytes]))
        #array1 = [ 'x.join(map(str, split_stream[0:150]))' , 'x.join(map(str, split_stream[150:300]))', 'x.join(map(str, split_stream[300:450]))']
        im[0] = 'ID1.1 '
        im[1] = 'ID1.2 '
        im[2] = 'ID1.3 '
        im[3] = 'ID1.4 '
        im[4] = 'ID1.5 '
        im[5] = 'ID1.6 '
        im[6] = 'ID1.7 '
       	t = open("/home/pi/pic4.txt", "a")
        #t.write("1: " + split_streamArray[0] + "\n2: " +  split_streamArray[1] + "\n3: " + split_streamArray[2] + "\n4:    " +  split_streamArray[3] + "\n5:  " + split_stream[4])
        t.close()
        #t.write(str(split_stream))
        #t.close()
        #print("1:   " + split_stream1)
        #print("2:   " + split_stream2)
        #print("3:   " + split_stream3)
        #print("4:   " + split_stream4)
        #print("5:   " + split_stream5)

        self.ser.write("AT+SBDWT=[Start]\r".encode())
        sleep(1)
        p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
        print(p)
        print(" image")
        self.ser.write('AT+SBDIX\r'.encode())
        sleep(2)
        p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
        print(p)
        print(" image")
        self.ser.write(b'AT+SBDD0\r')
        sleep(.1)
        p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
        print(p)
        print(" image")
        x =0
                
        while split_stream:
            while True:
                while x == 1:
                    test = 'AT+SBDWT=[' + split_stream1
                    #print(len(picData))
                    self.ser.write(str(test).encode()  + ']\r'.encode())
                    sleep(2)
                    print(" image just sent")
                    self.ser.write('\r'.encode())
                    self.ser.write('AT+SBDIX\r'.encode())
                    sleep(2)
                    p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
                    print(p)
                    self.ser.write('AT+SBDD0\r'.encode())
                    sleep(.1)
                    p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
                    print(p)
                    print(" image")
                    #del split_stream[0:150]
                    x += 1
				while x == 2:
					test = 'AT+SBDWT=[' + split_stream1
                    #print(len(picData))
                    self.ser.write(str(test).encode()  + ']\r'.encode())
                    sleep(2)
                    print(" image just sent")
                    self.ser.write('\r'.encode())
                    self.ser.write('AT+SBDIX\r'.encode())
                    sleep(2)
                    p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
                    print(p)
                    self.ser.write('AT+SBDD0\r'.encode())
                    sleep(.1)
                    p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
                    print(p)
                    print(" image")
                    #del split_stream[0:150]
                    x += 1
					
        self.ser.write("AT+SBDWT=[Stop]\r".encode())
        sleep(1)
        p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
        print(p)
        print(" image")
        self.ser.write('AT+SBDIX\r'.encode())
        sleep(2)
        p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
        print(p)
        print(" image")
        self.ser.write(b'AT+SBDD0\r')
        sleep(.1)
        p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
        print(p)
        print(" image")


    def register(self):
        while True:
            self.ser.write(b'AT+SBDREG')
            sleep(.5)
            p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
            print(p)
            print(" reg")


    def broadcast(self):
        while True:
            self.ser.write('AT+SBDWT=(Hello World)\r'.encode()) 
            p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
            print(p)
            sleep(1)
            print(" broadcast")
            self.ser.write('AT+SBDIX\r'.encode())
            p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
            print(p)
            sleep(2)
            print(" broadcast")
            self.ser.write(b'AT+SBDD0\r')
            p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
            print(p)
            sleep(.1)
            print(" broadcast")

    def send_message(self, laser_p):
        self.ser.write("AT+SBDWT=(" + laser_p.recv() + ")\r".encode())
        print("laser data: " + laser_p.recv())
        sleep(1)
        p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
        print(p)
        print(" laser")
        self.ser.write('AT+SBDIX\r'.encode())
        sleep(2)
        p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
        print(p)
        print(" laser")
        self.ser.write(b'AT+SBDD0\r')
        sleep(.1)
        p = self.ser.read(size=self.ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
        print(p)
        print(" laser")

def capture_picture(stream_c):
    camera = picamera.PiCamera()
    camera.exposure_mode = 'antishake'
    camera.resolution = (1025, 768)
#    camera.rotation = (180)
#    camera.annotate_text = 'RockSatX/U2Pi 2018' 
    sleep(2)
    index = 0
    maximum = 135

    for x in range(3):
        #file = open('/home/pi/image.jpg', 'wb')

        #camera.capture(file, resize=(19, 19))
        #file.close()

        file = open('/home/pi/image.jpg', 'rb')
        stream_c.send_bytes(file.read())
        file.close()

    while index < maximum:
        camera.capture("/home/pi/Pictures/pic" + str(index + 1) + ".png")
        sleep(5)
        index += 1

