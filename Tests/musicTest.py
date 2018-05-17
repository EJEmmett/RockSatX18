from pygame import mixer
from time import sleep as s

file = 'file1 = '/home/pi/Music/hoe_cakes.mp3'

mixer.init()
mixer.music.load(file)#the ONE rap song...
mixer.music.play()
