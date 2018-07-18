from time import sleep
from multiprocessing import Process, Array
import RPi.GPIO as GPIO

def main():
    #Internal Clock initialization
    time = Array("i", 2)
    timings = Process(target=increment, args=(time,))
    timings.start()

    o = open("/home/pi/masterLog.txt", "a+")

    # Set mode to physical pin slot
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    # Assign Pin 7 as output
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)

    #50 indicates HZ signal
    #Period of signal is 20 milliseconds
    p = GPIO.PWM(18, 50)
    #DutyCycle = PulseWidth/(1/frequency) = PulseWidth * frequency

    sleep(147)

    move = Process(target=movement, args=(p, o, time,))
    move.start()
    sleep(753)
    move.terminate()
    timings.terminate()
    p.stop()
    GPIO.cleanup()
    o.close()

def increment(t):
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

def movement(p, o, time):
    p.start(7.5)
    while 1:
        # Change to open
        p.ChangeDutyCycle(7.5)
        o.write("The servo moved at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
        #wait for open
        GPIO.output(4, GPIO.HIGH)
        o.write("The LED turned on at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
        sleep(3)
        # Return to closed
        p.ChangeDutyCycle(10)
        o.write("The servo moved at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
        sleep(3)
        p.ChangeDutyCycle(2.5)
        o.write("The servo moved at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
        GPIO.output(4, GPIO.LOW)
        o.write("The LED turned off at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')

main()
