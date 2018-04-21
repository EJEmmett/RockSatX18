import classModule
from time import sleep
from multiprocessing import Process, SimpleQueue
iridium = classModule.Iridium()

with classModule.Lasers() as lasers:
    q = SimpleQueue()
    laserList = Process(target=lasers.measure, args=(q,))
    laserList.start()
    while 1:
        iridium.sendMessage(q.get())
