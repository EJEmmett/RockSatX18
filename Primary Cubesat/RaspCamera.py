import picamera
from time import sleep
max = 125

sleep(125)
with picamera.PiCamera() as camera:
    camera.exposure_mode = 'antishake'
    while(max != 0):
        camera.capture_continuous('{timestamp:%H%M%S}-{counter:03d}.png')
        sleep(7)
        max-=1
    break
