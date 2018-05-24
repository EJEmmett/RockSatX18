from time import sleep
import RPi.GPIO as GPIO

def main():
    i = 0
    #sleep(79)

    # Set mode to physical pin slot
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    # Assign Pin 7 as output
    GPIO.setup(18, GPIO.OUT)

    #50 indicates HZ signal
    #Period of signal is 20 milliseconds
    p=GPIO.PWM(18, 50)
    #DutyCycle = PulseWidth/(1/frequency) = PulseWidth * frequency
    p.start(7.5)

    while (i < 10):
        # Change to open
        p.ChangeDutyCycle(7.5)
        #wait for open
        sleep(1)#this is the time that I thought we decided on?
        # Return to closed
        p.ChangeDutyCycle(10)
        sleep(1)
        p.ChangeDutyCycle(2.5)
        i += 1
    p.stop()
    GPIO.cleanup()

main()
