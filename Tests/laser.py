from laserTests import Iridium, Laser, Clock, Music, cap
from multiprocessing import Pipe, Process, Array
from time import sleep

def main():
    #time = Array("i", 2)
    #music = Music()
    #clock = Clock()
    #iridium = Iridium()
    #laser = Laser()
    #print("Class Instancing")

    #broadcast = Process(target=iridium.broadcast)
    #laserList = Process(target=laser.measure)
    #timings = Process(target=clock.increment, args=(time,))
    snapshots = Process(target=cap)
    #muzzak = Process(target=music.begin)
    #print("Process Instancing")

    #timings.start()
    #muzzak.start()
    #broadcast.start()
    #print("Timings, Muzzak, and broadcast start")

    #sleep(10)

    #broadcast.terminate()
    #print("Broadcast Stop")

    #laserList.start()
    snapshots.start()
    #print("Laser and Snapshot start")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
