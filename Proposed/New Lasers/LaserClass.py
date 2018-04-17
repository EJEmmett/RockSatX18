import time
import VL53L0X
import RPi.GPIO as GPIO

class Lasers(object):
    def __init__(self):
        GPIO.setwarnings(False)
        lasor1_shutdown = 20
        lasor2_shutdown = 16

        #Assign Shutdown pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)

        #Shutdown Lasers to reset
        GPIO.output(lasor1_shutdown, GPIO.LOW)
        GPIO.output(lasor2_shutdown, GPIO.LOW)

        #Sleep to ensure reset
        time.sleep(0.5)

        #Create Laser objects and assign addresses
        laser1 = VL53L0X.VL53L0X(address=0x1)
        laser2 = VL53L0X.VL53L0X(address=0x2)

        #Start Laser 1 and begin ranging
        GPIO.output(lasor1_shutdown, GPIO.HIGH)
        time.sleep(0.50)
        laser1.start_ranging(VL53L0X.VL53L0X_HIGH_SPEED_MODE)

        #Start laser 2 and begin ranging
        GPIO.output(lasor2_shutdown, GPIO.HIGH)
        time.sleep(0.50)
        laser2.start_ranging(VL53L0X.VL53L0X_HIGH_SPEED_MODE)

    def __enter__(self):

    def measure(self):
        distance1 = laser1.get_distance()
        distance2 = laser2.get_distance()
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
            laser2.stop_ranging()
            GPIO.output(lasor2_shutdown, GPIO.LOW)
            laser1.stop_ranging()
            GPIO.output(lasor1_shutdown, GPIO.LOW)
