from laserTests import Iridium, Laser, Clock, Music, cap
from multiprocessing import Pipe, Process, Array
from time import sleep

def main():
    time = Array("i", 2)
    music = Music()
    clock = Clock()
    iridium = Iridium()
    laser = Laser()

    broadcast = Process(target=iridium.broadcast)
    laserList = Process(target=laser.measure)
    timings = Process(target=clock.increment, args=(time,))
    snapshots = Process(target=cap)
    muzzak = Process(target=music.begin)

    timings.start()
    muzzak.start()
    broadcast.start()

    sleep(10)

    broadcast.terminate()

    laserList.start()
    snapshots.start()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
