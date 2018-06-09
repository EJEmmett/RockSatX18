from laserTests import Iridium, Laser, Clock, Camera, Music
from multiprocessing import Pipe, Process, Array
from time import sleep
import psutil

def main():
    parent, child = Pipe()
    music = Music()
    camera = Camera()
    clock = Clock()
    iridium = Iridium()
    laser = Laser()

    broadcast = Process(target=iridium.broadcast)
    laserList = Process(target=laser.measure, args=(child,))
    timings = Process(target=clock.increment, args=(time,))
    snapshots = Process(target=camera.picture)
    muzzak = Process(target=music.begin)

    timings.start()
    muzzak.start()
    broadcast.start()
    laserList.start()
    snapshots.start()

    sleep(200)

    broadcast.join()

    print(psutil.cpu_percent())
    print(psutil.virtual_memory())

    while True:
        iridium.sendMessage(parent.recv())
        print(psutil.cpu_percent())
        print(psutil.virtual_memory())

if __name__ == '__main__':
    main()
