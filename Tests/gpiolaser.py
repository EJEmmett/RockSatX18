from time import sleep
from ST_VL6180X import VL6180X

#Create Laser objects and assign addresses
laser = VL6180X(address=0x29)
laser.default_settings()

while 1:
    print(laser.get_distance())
