from functions import Laser, Iridium, Clock
from time import sleep
from multiprocessing import Process, Pipe, Array

def main:
    #Class instancing
    o = open("/home/pi/masterLog.txt", "a+")

    clock = Clock()
    iridium = Iridium()
    laser = Laser()

    #Laser pipe initialization
    parent, child = Pipe()

    #Time initialization
    time = Array("i", 2)

    #Process initialization
    laserList = Process(target=lasers.measure, args=(child, time,))
    broadcast = Process(target=iridium.broadcast)
    timings = Process(target=clock.increment, args=(time,))
    timings.start()
    laserList.start()
    broadcast.start()

    sleep(200)

    #Process close
    broadcast.join()

    while True:
        o.write("The iridium started sending at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
        iridium.sendMessage(parent.recv())
        o.write("The iridium stopped sending at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
        
if __name__ == '__main__':
    main()
