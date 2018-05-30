from pygame import mixer
from time import sleep, strftime

log = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
log[0] = "The music started playing at: "
log[1] = "Song 1 started playing at: "
log[2] = "Song 1 stopped playing at:"
log[3] = "Song 2 started playing at: "
log[4] = "Song 2 stopped playing at:"
log[5] = "Song 3 started playing at: "
log[6] = "Song 3 stopped playing at:"
log[7] = "Song 4 started playing at: "
log[8] = "Song 4 stopped playing at: "
log[9] = "Song 5 started playing at: "
log[10] = "Song 5 stopped playing at: "
log[11] =  "The music stopped playing at: "
o = open("masterLog.txt", "a+")

file1 = '/home/pi/Music/danger_zone.mp3'
file2 = '/home/pi/Music/Starman.mp3'
file3 = '/home/pi/Music/cakes.mp3'
file4 = '/home/pi/Music/staying_alive.mp3'
file5 = '/home/pi/Music/space_oddity.mp3'

mixer.init()
o.write(log[0] + strftime('%H:%M:%S') + '\n')
sleep(0.1)
o.write(log[1] + strftime('%H:%M:%S') + '\n')
mixer.music.load(file1)
mixer.music.play()
sleep(180)
o.write(log[2] + strftime('%H:%M:%S') + '\n')
sleep(0.1)

o.write(log[3] + strftime('%H:%M:%S') + '\n')
sleep(0.1)
mixer.music.load(file2)
mixer.music.play()
sleep(180)
o.write(log[4] + strftime('%H:%M:%S') + '\n')
sleep(0.1)

o.write(log[5] + strftime('%H:%M:%S') + '\n')
sleep(0.1)
mixer.music.load(file3)#the ONE rap song...
mixer.music.play()
sleep(180)
o.write(log[6] + strftime('%H:%M:%S') + '\n')
sleep(0.1)

o.write(log[7] + strftime('%H:%M:%S') + '\n')
sleep(0.1)
mixer.music.load(file4)
mixer.music.play()
sleep(180)
o.write(log[8] + strftime('%H:%M:%S') + '\n')
sleep(0.1)

o.write(log[9] + strftime('%H:%M:%S') + '\n')
sleep(0.1)
mixer.music.load(file5)
mixer.music.play()
sleep(180)
o.write(log[10] + strftime('%H:%M:%S') + '\n')
sleep(0.1)
o.write(log[11] + strftime('%H:%M:%S') + '\n')

mixer.stop()
