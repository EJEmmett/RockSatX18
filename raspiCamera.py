import picamera
from time import sleep
import os
camera = picamera.PiCamera()
pictureFileName = "pic#.jpg"
outputVersion = 1
index = 0
max = 125

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

time.sleep(80)
while(index < max):
	pictureFileName = pictureFileName.replace("#", str(outputVersion))
	camera.capture("pic#.jpg")
	index += 1
	outputVersion += 1
	time.sleep(7)