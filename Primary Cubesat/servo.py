from time import sleep
import RPi.GPIO as GPIO

# Set mode to physical pin slot
GPIO.setmode(GPIO.BOARD)
# Assign Pin 7 as output
GPIO.setup(7, GPIO.OUT)

#50 indicates HZ signal
#Period of signal is 20 milliseconds
p = GPIO.PWM(7, 50)
#DutyCycle = PulseWidth/(1/frequency) = PulseWidth * frequency
p.start(5)

while True:
    # Change to open
    p.ChangeDutyCycle(10)
    #wait for open
    sleep(.4)
    # Return to closed
    p.ChangeDutyCycle(5)

p.stop()
GPIO.cleanup()
