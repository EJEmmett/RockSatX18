import picamera
from time import sleep
import os
camera = picamera.PiCamera()
pictureFileName = "pic#.jpg"
outputVersion = 1
index = 0
max = 10

camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.video_stabilization = False
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
camera.rotation = 0
camera.hflip = False
camera.vflip = False
camera.crop = (0.0, 0.0, 1.0, 1.0)

sleep(2)
while(index < max):
    pictureFileName1 = pictureFileName.replace("#", str(outputVersion))
    camera.capture(pictureFileName1)
    index += 1
    outputVersion += 1
    sleep(2)

