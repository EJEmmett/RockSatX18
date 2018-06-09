import picamera
from time import sleep
from multiprocessing import Process, Array

class Clock:
    def __init__(self):
        self.second = 0
        self.minute = 0

    def increment(self, t):
        while 1:
            self.second+=1
            if self.second == 60:
                self.minute+=1
                self.second = 0
            t[0] = self.minute
            t[1] = self.second
            sleep(1)

def main():
    #Internal Clock initialization
    clock = Clock()
    time = Array("i", 2)
    timings = Process(target=clock.increment, args=(time,))
    timings.start()

    camera = picamera.PiCamera()
    outputVersion = 1
    index = 0
    max = 135
    camera.exposure_mode = 'antishake'

    o = open("/home/pi/masterLog.txt", "a+")

    sleep(79)
    while(index < max):
        camera.capture("/home/pi/Pictures/pic" + outputVersion + ".png")
        o.write("The camera took a picture at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
        index += 1
        outputVersion += 1
        sleep(15)

    o.close()
    timings.join()

if __name__ == '__main__':
    main()
