from laserTests import Iridium, Laser

def main():
    laser = Laser()
    laser.measure()

    iridium = Iridium()
    iridium.sendMessage("HI")
main()
