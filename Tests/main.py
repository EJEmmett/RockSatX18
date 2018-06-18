from time import sleep
from multiprocessing import Pipe, Process, Array
from laserTests import Iridium, Laser, clock, cap

def main():
    file = open("/home/pi/masterLog.txt", "a+")

    time = Array("i", 2)
    parent, child = Pipe()
    iridium = Iridium()
    laser = Laser()

    timings = Process(target=clock, args=(time,))
    broadcast = Process(target=iridium.broadcast)
    laser_list = Process(target=laser.measure, args=(time, child,))
    snapshots = Process(target=cap)

    timings.start()
    broadcast.start()

    sleep(70)
    snapshots.start()
    sleep(37)
    laser_list.start()
    sleep(93)
    broadcast.terminate()

    while 1:
        file.write("The iridium started sending at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
        iridium.sendMessage(parent.recv())
        file.write("The iridium stopped sending at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')

if __name__ == '__main__':
    main()
