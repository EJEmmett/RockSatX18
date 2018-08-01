from time import sleep
from io import BytesIO
import serial
import minimalmodbus as mini
import picamera
import base64

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

    def measure(self, t):
		laserFile = open("/home/pi/laser.log", "a+")
        while 1:
            primary_pass = self.primary_instrument.read_register(24, functioncode=4)
            instance = None

            if primary_pass is not 0:
                instance = primary_pass

            if instance is None:
                laser_c.send("Laser passed at " + str(t[0]).zfill(2) + ":" + str(t[1]).zfill(2) + "          ")#31 Bytesw   
                laserFile(laser_c.send)
				
class Iridium:
    def __init__(self):
        try:
            self.ser = serial.Serial(port="/dev/ttyUSB1", baudrate=19200, xonxoff=True)
        except:
            self.ser = serial.Serial(port="/dev/ttyUSB0", baudrate=19200, xonxoff=True)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
    
    def image_transmission(self):
        with open("/home/pi/image.jpg", "rb") as image:
            encoded = base64.b64encode(image.read())
        self.ser.write("AT+SBDWT=[Start]".encode())
        sleep(.1)
        self.ser.write("AT+SBDIX\r".encode())
        sleep(.1)
        self.ser.write("AT+SBDD0\r".encode())
		
		y = 0
        s1 = "AT+SBDWT=".encode()  + encoded[0:85]
        s2 = "AT+SBDWT=".encode()  + encoded[85:170]
        s3 = "AT+SBDWT=".encode()  + encoded[170:255]
        s4 = "AT+SBDWT=".encode()  + encoded[255:340]
        s5 = "AT+SBDWT=".encode()  + encoded[340:425]
        s6 = "AT+SBDWT=".encode()  + encoded[425:510]
        s7 = "AT+SBDWT=".encode()  + encoded[510:595]
        s8 = "AT+SBDWT=".encode()  + encoded[595:680]
        s9 = "AT+SBDWT=".encode()  + encoded[680:765]
        s10 = "AT+SBDWT=".encode()  + encoded[765:850]
        s11 = "AT+SBDWT=".encode()  + encoded[850:935]
        s12 = "AT+SBDWT=".encode()  + encoded[935:1020]
        s13 = "AT+SBDWT=".encode()  + encoded[1020:1105]
        s14 = "AT+SBDWT=".encode()  + encoded[1105:1190]
        s15 = "AT+SBDWT=".encode()  + encoded[1190:1275]
        s16 = "AT+SBDWT=".encode()  + encoded[1275:1360]
        s17 = "AT+SBDWT=".encode()  + encoded[1360:1445]
                
        
        while y != 12:
            len(encoded)
            for number in range(4):
                print("1")
                self.ser.write(s1 + "[1\r".encode())    
                sleep(2)
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)

                self.ser.write("AT+SBDD0\r".encode())
                sleep(4)
            
            for number in range(4):
                print("2")
                self.ser.write(s2 + "[2\r".encode()) 
                sleep(2)  
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)
            
                self.ser.write("AT+SBDD0\r".encode())
                sleep(4)
            
            for number in range(4):
                print("3")
                self.ser.write(s3 + "[3\r".encode())
                sleep(2)    
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)
            
            self.ser.write("AT+SBDD0\r".encode())
            sleep(4)
           
            for number in range(4):
                print("4")
                self.ser.write(s4 + "[4\r".encode()) 
                sleep(2)    
                self.ser.write("AT+SBDIX\r".encode()))
                sleep(1)
               
				self.ser.write("AT+SBDD0\r".encode())
				sleep(4)
            
            for number in range(4):
                print("5")
                self.ser.write(s5 + "[5\r".encode()) 
                sleep(2)    
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)
               
                self.ser.write("AT+SBDD0\r".encode())
                sleep(4)
            
            for number in range(4):
                self.ser.write(s6 + "[6\r".encode())
                sleep(2)    
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)
            
				self.ser.write("AT+SBDD0\r".encode())
				sleep(4)

            for number in range(4):
                self.ser.write(s7 + "[7\r".encode())
                sleep(2)    
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)

            
            self.ser.write("AT+SBDD0\r".encode())
            sleep(4)

            for number in range(4):
                self.ser.write(s8 + "[8\r".encode())
                sleep(2)    
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)

            
            self.ser.write("AT+SBDD0\r".encode())
            sleep(4)
            
            for number in range(4):
                self.ser.write(s9 + "[9\r".encode()) 
                sleep(2)
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)

                self.ser.write("AT+SBDD0\r".encode())
                sleep(4)    
                
            for number in range(4):
                self.ser.write(s10 + "[10\r".encode())
                sleep(2)   
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)
              
            self.ser.write("AT+SBDD0\r".encode())
            sleep(4)
           
            for number in range(4):
                self.ser.write(s11 + "[11\r".encode()) 
                sleep(2)   
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)
              
            self.ser.write("AT+SBDD0\r".encode())
            sleep(4)
            
            for number in range(4):
                self.ser.write(s12 + "[12\r".encode())
                sleep(2)    
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)
              
            self.ser.write("AT+SBDD0\r".encode())
            sleep(4)
            
            for number in range(4):
                self.ser.write(s13 + "[13\r".encode())
              
            self.ser.write("AT+SBDD0\r".encode())
            sleep(4)
            
            for number in range(4):
                self.ser.write(s14 + "[14\r".encode())  
                sleep(2)
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)
              
         
            self.ser.write("AT+SBDD0\r".encode())
            sleep(4)
           
            for number in range(4):
                self.ser.write(s15 + "[15\r".encode()) 
                sleep(2)    
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)
         
            self.ser.write("AT+SBDD0\r".encode())
            sleep(4)
            
            for number in range(4):
                self.ser.write(s16 + "[16\r".encode()) 
                sleep(2)    
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)
              
            self.ser.write("AT+SBDD0\r".encode())
            sleep(4)
            

            for number in range(4):
                self.ser.write(s17 + "[17\r".encode()) 
                sleep(2)    
                self.ser.write("AT+SBDIX\r".encode())
                sleep(1)
              
            self.ser.write("AT+SBDD0\r".encode())
            sleep(4)
            y += 1



        self.ser.write("AT+SBDWT=[Stop]".encode())
        sleep(1)
        self.ser.write(b"AT+SBDIX\r")
        sleep(2)
        self.ser.write("AT+SBDD0\r".encode())

    def register(self):
        while True:
            self.ser.write("AT+SBDREG".encode())
            sleep(.1)

    def broadcast(self):
        while True:
            self.ser.write("AT+SBDWT=[B2:I'm alive]\r".encode()) #31 Bytes
            sleep(1)
            self.ser.write("AT+SBDIX\r".encode())
            sleep(2)
            self.ser.write("AT+SBDD0\r".encode())

        
def capture_picture():
    camera = picamera.PiCamera()
    camera.exposure_mode = 'antishake'
    camera.resolution = (1025, 768)
        
    sleep(2)
    index = 0
    maximum = 135

    for x in range(3):
        file = open('/home/pi/image.jpg', 'wb')
        camera.capture(file, resize=(15, 15))
        file.close()

    while index < maximum:
        camera.capture("/home/pi/Pictures/pic" + str(index + 1) + ".png")
        index += 1
        sleep(5)
