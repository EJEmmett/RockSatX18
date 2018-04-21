import time
import serial
import VL53L0X
import RPi.GPIO as GPIO

class Lasers(object):
    def __init__(self):
        self.GPIO.setwarnings(False)
        lasor1_shutdown = 20
        lasor2_shutdown = 16

        #Assign Shutdown pins
        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setup(20, GPIO.OUT)
        self.GPIO.setup(16, GPIO.OUT)

        #Shutdown Lasers to reset
        self.GPIO.output(lasor1_shutdown, GPIO.LOW)
        self.GPIO.output(lasor2_shutdown, GPIO.LOW)

        #Sleep to ensure reset
        time.sleep(0.5)

        #Create Laser objects and assign addresses
        self.laser1 = VL53L0X.VL53L0X(address=0x1)
        self.laser2 = VL53L0X.VL53L0X(address=0x2)

        #Start Laser 1 and begin ranging
        self.GPIO.output(lasor1_shutdown, 1)
        time.sleep(0.50)
        self.laser1.start_ranging(VL53L0X.VL53L0X_HIGH_SPEED_MODE)

        #Start laser 2 and begin ranging
        self.GPIO.output(lasor2_shutdown, 1)
        time.sleep(0.50)
        self.laser2.start_ranging(VL53L0X.VL53L0X_HIGH_SPEED_MODE)

    def __enter__(self):

    def measure(self):
        distance1 = self.laser1.get_distance()
        distance2 = self.laser2.get_distance()
        if (distance1 < 100):
            instance = ('Laser One passed at: {}'.format(time.strftime('%H:%M:%S')))
            time.sleep(.5)
        elif (distance2 < 100):
            instance = ('Laser Two passed at: {}'.format(time.strftime('%H:%M:%S')))
            time.sleep(.5)
        if instance:
            with open("Lasers.txt", "a") as f:
                f.write(instance+"\n")

        return instance

    def __exit__(self):
        self.laser2.stop_ranging()
        self.GPIO.output(lasor2_shutdown, GPIO.LOW)
        self.laser1.stop_ranging()
        self.GPIO.output(lasor1_shutdown, GPIO.LOW)

class Iridium(object):
    def __init__(self):
        self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=19200, xonxoff=True)
        self.ser.close()
        self.ser.open()

    def sendMessage(self, m):
        if(!m):
            pass

        self.ser.write('AT+SDBWT={}\r'.format(m).encode())
        sleep(1)
        self.ser.write('AT+SBDIX\r'.encode())
        returned = self.ser.read(self.ser.in_waiting).strip().split('\n')

        if(isinstance(returned,list) and len(returned)>1):
            if(len(returned)>2):
                if(returned[1]!='0'):
                    self.sendMessage(m)
        else:
            self.sendMessage(m)

        return returned
