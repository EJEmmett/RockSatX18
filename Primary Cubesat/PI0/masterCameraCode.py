import picamera
from time import sleep, strftime

camera = picamera.PiCamera()
outputVersion = 1
index = 0
max = 35
camera.exposure_mode = 'antishake'

log = ["The camera took a picture at: "]
o = open("masterLog.txt", "a+")

sleep(2)
while(index < max):
    camera.capture("pic" + outputVersion + ".jpg")
    o.write(log[1] + time.strftime('%H:%M:%S') + '\n')
    index += 1
    outputVersion += 1
    sleep(7)

    o.close()
