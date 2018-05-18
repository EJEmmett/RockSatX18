from functions import Iridium, Laser
from time import sleep
from multiprocessing import Process, Queue

def main():
    #Class instancing
    try:
        iridium = Iridium("/dev/ttyUSB0")
        lasers = Laser("/dev/ttyUSB1")
    except Exception:
        iridium = Iridium("/dev/ttyUSB1")
        lasers = Laser("/dev/ttyUSB0")

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
