import serial
import classModule
from time import sleep
iridium = classModule.Iridium()

with classModule.Lasers() as lasers:
    while 1:
        iridium.sendMessage(lasers.measure())
