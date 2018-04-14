import picamera
from time import sleep
camera = picamera.PiCamera()
pictureFileName = "pic#.jpg"
outputVersion = 1
index = 0
max = 125


camera.exposure_mode = 'antishake'

sleep(125)
while(index < max):
    pictureFileName1 = pictureFileName.replace("#", str(outputVersion))
    camera.capture_continuous(pictureFileName1)
    index += 1
    outputVersion += 1
    sleep(7)
break
