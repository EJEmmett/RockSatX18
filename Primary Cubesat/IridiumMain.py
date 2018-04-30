from minimalLasers import Iridium, Laser
from subprocess import call
from time import sleep
from multiprocessing import Process, SimpleQueue

#Disable USB while launching
call(["echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/unbind"])
sleep(20)
call(["echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/bind"])
sleep(10)
#Class instancing
iridium = Iridium()
lasers = Laser()
q = SimpleQueue()

#Process initialization
laserList = Process(target=lasers.measure, args=(q,))
broadcast = Process(target=iridium.broadcast)
laserList.start()
broadcast.start()

sleep(50)

#Process close
broadcast.join()

while 1:
    iridium.sendMessage(q.get())
