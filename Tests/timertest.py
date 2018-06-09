from multiprocessing import Process, Array
from time import sleep
from timer import Clock

if __name__ == '__main__':
    timer = Clock()
    time = Array("i", 2)

    clocker = Process(target=timer.increment, args=(time,))
    clocker.start()
    sleep(4)
    print(str(time[0]).zfill(2)+":"+str(time[1]).zfill(2))
    clocker.join()
