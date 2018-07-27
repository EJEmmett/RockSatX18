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
        im = [1, 2, 3, 4, 5, 6, 7]
        print("split stream 1:" +  str(split_stream[0:1])) 
        s1 = ''.join(map(str, split_stream[0:80]))
        s2 = ''.join(map(str, split_stream[80:160]))
        s3 = ''.join(map(str, split_stream[240:320]))
        s4 = ''.join(map(str, split_stream[320:400]))
        s5 = ''.join(map(str, split_stream[400:480]))
        s6 = ''.join(map(str, split_stream[480:560]))
        s7 = ''.join(map(str, split_stream[560:640]))
        s8 = ''.join(map(str, split_stream[640:720]))
        s9 = ''.join(map(str, split_stream[720:800]))
        s10 = ''.join(map(str, split_stream[800:880]))
        s11 = ''.join(map(str, split_stream[880:960]))
		s13 = ''.join(map(str, split_stream[960:1040]))
        s14 = ''.join(map(str, split_stream[1040:1120]))
        s15 = ''.join(map(str, split_stream[1120:1200]))
        s16 = ''.join(map(str, split_stream[1200:1280]))
        s17 = ''.join(map(str, split_stream[1280:1360]))
        s18 = ''.join(map(str, split_stream[1360:1440]))
        s19 = ''.join(map(str, split_stream[1440:1520]))
        s20 = ''.join(map(str, split_stream[1520:1600]))
        s21 = ''.join(map(str, split_stream[1600:1680]))
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
        x = 1 
                
        while split_stream:
            while True:
                test = 'AT+SBDWT=[P1:' + s1
                self.ser.write(str(test).encode()  + ']\r'.encode())
                sleep(1)
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
                test = 'AT+SBDWT=[P2' + s2
                self.ser.write(str(test).encode()  + ']\r'.encode())
                sleep(1)
                print(" image just sent")
                self.ser.write('\r'.encode())
                self.ser.write('AT+SBDIX\r'.encode())
                sleep(2)
                self.ser.write('AT+SBDD0\r'.encode())
                sleep(.1)
				test = 'AT+SBDWT=[P3' + s3
                self.ser.write(str(test).encode()  + ']\r'.encode())
                sleep(1)
                print(" image just sent")
                self.ser.write('\r'.encode())
                self.ser.write('AT+SBDIX\r'.encode())
                sleep(2)
                self.ser.write('AT+SBDD0\r'.encode())
                sleep(.1)
				test = 'AT+SBDWT=[P3' + s3
                self.ser.write(str(test).encode()  + ']\r'.encode())
                sleep(1)
                print(" image just sent")
                self.ser.write('\r'.encode())
                self.ser.write('AT+SBDIX\r'.encode())
                sleep(2)
                self.ser.write('AT+SBDD0\r'.encode())
                sleep(.1)
				test = 'AT+SBDWT=[P4' + s4
                self.ser.write(str(test).encode()  + ']\r'.encode())
                sleep(1)
                print(" image just sent")
                self.ser.write('\r'.encode())
                self.ser.write('AT+SBDIX\r'.encode())
                sleep(2)
                self.ser.write('AT+SBDD0\r'.encode())
                sleep(.1)
				test = 'AT+SBDWT=[P5' + s5
                self.ser.write(str(test).encode()  + ']\r'.encode())
                sleep(1)
                print(" image just sent")
                self.ser.write('\r'.encode())
                self.ser.write('AT+SBDIX\r'.encode())
                sleep(2)
                self.ser.write('AT+SBDD0\r'.encode())
                sleep(.1)
				test = 'AT+SBDWT=[P6' + s6
                self.ser.write(str(test).encode()  + ']\r'.encode())
                sleep(1)
                print(" image just sent")
                self.ser.write('\r'.encode())
                self.ser.write('AT+SBDIX\r'.encode())
                sleep(2)
                self.ser.write('AT+SBDD0\r'.encode())
                sleep(.1)
				test = 'AT+SBDWT=[P7' + s7
                self.ser.write(str(test).encode()  + ']\r'.encode())
                sleep(1)
                print(" image just sent")
                self.ser.write('\r'.encode())
                self.ser.write('AT+SBDIX\r'.encode())
                sleep(2)
                self.ser.write('AT+SBDD0\r'.encode())
                sleep(.1)
				test = 'AT+SBDWT=[P8' + s8
                self.ser.write(str(test).encode()  + ']\r'.encode())
                sleep(1)
                print(" image just sent")
                self.ser.write('\r'.encode())
                self.ser.write('AT+SBDIX\r'.encode())
                sleep(2)
                self.ser.write('AT+SBDD0\r'.encode())
                sleep(.1)
				test = 'AT+SBDWT=[P9' + s9
                self.ser.write(str(test).encode()  + ']\r'.encode())
                sleep(1)
                print(" image just sent")
                self.ser.write('\r'.encode())
                self.ser.write('AT+SBDIX\r'.encode())
                sleep(2)
                self.ser.write('AT+SBDD0\r'.encode())
                sleep(.1)
				test = 'AT+SBDWT=[P10' + s10
                self.ser.write(str(test).encode()  + ']\r'.encode())
                sleep(1)
                print(" image just sent")
                self.ser.write('\r'.encode())
                self.ser.write('AT+SBDIX\r'.encode())
                sleep(2)
                self.ser.write('AT+SBDD0\r'.encode())
                sleep(.1)
				test = 'AT+SBDWT=[P11' + s11
                self.ser.write(str(test).encode()  + ']\r'.encode())
                sleep(1)
                print(" image just sent")
                self.ser.write('\r'.encode())
                self.ser.write('AT+SBDIX\r'.encode())
                sleep(2)
                self.ser.write('AT+SBDD0\r'.encode())
                sleep(.1)
         

                
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
