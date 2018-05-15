from functions import Iridium, Laser
from time import sleep
from multiprocessing import Process, Queue

def main():
    #Class instancing
    iridium = Iridium()
    lasers = Laser()
    laserQueue = Queue()

    #Process initialization
    laserList = Process(target=lasers.measure, args=(laserQueue,))
    broadcast = Process(target=iridium.broadcast)
    laserList.start()
    broadcast.start()

    sleep(200)

    #Process close
    broadcast.join()

    while True:
        iridium.sendMessage(laserQueue.get())

main()
