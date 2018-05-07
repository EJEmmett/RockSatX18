from minimalLasers import Iridium, Laser
from time import sleep
from multiprocessing import Process, SimpleQueue

#Class instancing
iridium = Iridium()
lasers = Laser()
q = SimpleQueue()

#Process initialization
laserList = Process(target=lasers.measure, args=(q,))
broadcast = Process(target=iridium.broadcast)
laserList.start()
broadcast.start()

sleep(200)

#Process close
broadcast.join()

while 1:
    iridium.sendMessage(q.get())
