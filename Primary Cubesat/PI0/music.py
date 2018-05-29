import time
from pygame import mixer
from time import sleep as s

log = ["The music started playing at: ", "The music stopped playing at: "]
o = open("masterLog.txt", "a+")

file1 = '/home/pi/Music/danger_zone.mp3'
file2 = '/home/pi/Music/Starman.mp3'
file3 = '/home/pi/Music/cakes.mp3'
file4 = '/home/pi/Music/staying_alive.mp3'
file5 = '/home/pi/Music/space_oddity.mp3'

mixer.init()

o.write(log[1] + time.strftime('%H:%M:%S') + '\n')
mixer.music.load(file1)
mixer.music.play()
s(180)

mixer.music.load(file2)
mixer.music.play()
s(180)

mixer.music.load(file3)#the ONE rap song...
mixer.music.play()
s(180)

mixer.music.load(file4)
mixer.music.play()
s(180)

mixer.music.load(file5)
mixer.music.play()
o.write(log[1] + time.strftime('%H:%M:%S') + '\n')

#print("finished")
