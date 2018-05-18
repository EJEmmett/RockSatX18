import picamera
from time import sleep
camera = picamera.PiCamera()
outputVersion = 1
index = 0
max = 35
camera.exposure_mode = 'antishake'

sleep(2)
while(index < max):
    camera.capture("pic" + outputVersion + ".jpg")
    index += 1
    outputVersion += 1
    sleep(7)
