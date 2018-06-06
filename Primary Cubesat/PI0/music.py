from pygame import mixer
from time import sleep
from multiprocessing import Process, Array
from masterCameraCode import Clock

def main():
    #Internal Clock initialization
    clock = Clock()
    time = Array("i", 2)
    timings = Process(target=clock.increment, args=(time,))
    timings.start()

    o = open("/home/pi/masterLog.txt", "a+")

    file1 = '/home/pi/Music/danger_zone.mp3'
    file2 = '/home/pi/Music/Starman.mp3'
    file3 = '/home/pi/Music/cakes.mp3'
    file4 = '/home/pi/Music/staying_alive.mp3'
    file5 = '/home/pi/Music/space_oddity.mp3'

    mixer.init()
    o.write("The music started playing at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
    sleep(0.1)
    o.write("Song 1 started playing at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
    mixer.music.load(file1)
    mixer.music.play()
    sleep(180)
    o.write("Song 1 stopped playing at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
    sleep(0.1)

    o.write("Song 2 started playing at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
    sleep(0.1)
    mixer.music.load(file2)
    mixer.music.play()
    sleep(180)
    o.write("Song 2 stopped playing at:" + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
    sleep(0.1)

    o.write("Song 3 started playing at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
    sleep(0.1)
    mixer.music.load(file3)#the ONE rap song...
    mixer.music.play()
    sleep(180)
    o.write("Song 3 stopped playing at:" + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
    sleep(0.1)

    o.write("Song 4 started playing at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
    sleep(0.1)
    mixer.music.load(file4)
    mixer.music.play()
    sleep(180)
    o.write("Song 4 stopped playing at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
    sleep(0.1)

    o.write("Song 5 started playing at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
    sleep(0.1)
    mixer.music.load(file5)
    mixer.music.play()
    sleep(180)
    o.write("Song 5 stopped playing at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')
    sleep(0.1)
    o.write("The music stopped playing at: " + str(time[0]).zfill(2)+":"+str(time[1]).zfill(2) + '\n')

    mixer.stop()
    o.close()
    timings.close()

if __name__ == '__main__':
    main()
