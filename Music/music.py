from pygame import mixer
from time import sleep as s

file1 = '/home/pi/Music/'
file2 = '/home/pi/Music/'
file3 = 'home/pi/Music/hoe_cakes.mp3'
file4 = '/home/pi/Music/'
file5 = '/home/pi/Music/'

mixer.init()

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
mixer.stop()

mixer.music.load(file5)
mixer.music.play()

print("finished")
