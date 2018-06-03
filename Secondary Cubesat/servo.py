import RPi.GPIO as GPIO
from time import sleep, strftime
from multiprocessing import Process, Array

class Clock:
    def __init__(self):
        self.second = 0
        self.minute = 0

    def increment(self, t):
        self.second+=1
        if self.second == 60:
            self.minute+=1
            self.second = 0
        t[0] = self.minute
        t[1] = self.second
        sleep(1)

def main():
    #Internal Clock initialization
    clock = Clock()
    time = Array("i", 2)
    timings = Process(target=clock.increment, args=(time,))
    timings.start()

    #Servo movement

    o = open("masterLog.txt", "a+")
    i = 0

    # Set mode to physical pin slot
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    # Assign Pin 7 as output
    GPIO.setup(18, GPIO.OUT)

    #50 indicates HZ signal
    #Period of signal is 20 milliseconds
    p=GPIO.PWM(18, 50)
    #DutyCycle = PulseWidth/(1/frequency) = PulseWidth * frequency

    sleep(147)

    move = Process(target=movement, args=(p, o,))
    move.start()
    sleep(753)
    move.join()
    timings.join()
    p.stop()
    GPIO.cleanup()
    o.close()

def movement(p, o):
    p.start(7.5)
    while 1:
        # Change to open
        p.ChangeDutyCycle(7.5)
        o.write("The servo moved at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
        #wait for open
        sleep(1)#this is the time that I thought we decided on?
        # Return to closed
        p.ChangeDutyCycle(10)
        o.write("The servo moved at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
        sleep(1)
        p.ChangeDutyCycle(2.5)
        o.write("The servo moved at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
        i += 1

main()
