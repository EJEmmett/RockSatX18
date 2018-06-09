from laserTests import Iridium, Laser
from multiprocessing import Pipe
from time import sleep

def main():
    parent, child = Pipe()
    iridium = Iridium()
    laser = Laser()

    laser.measure(child)
    print(parent.recv())
    iridium.sendMessage("HI")
main()
