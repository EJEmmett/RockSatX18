from iridium import Iridium
from laser import Laser
from time import sleep, stftime
from multiprocessing import Process, Queue

def main:
    #Class instancing
    log = ["The iridium started sending at: ", "The iridium stopped sending at: ")
    o = open("masterLog.txt", "a+")
    try:
        iridium = Iridium("/dev/ttyUSB0")
    except Exception:
        iridium = Iridium("/dev/ttyUSB1")
        pass
    try:
        lasers = Laser("/dev/ttyUSB0")
    except Exception as e:
        lasers = Laser("/dev/ttyUSB1")

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
        o.write(log[1] + strftime('%H:%M:%S') + '\n')

main()
