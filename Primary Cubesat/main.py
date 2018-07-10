from time import sleep
from multiprocessing import Pipe, Process, Array
from functions import Iridium, Laser, capture_picture, clock

def main():
    file = open("/home/pi/masterLog.txt", "a+")

    t = Array("i", 2)
    laser_p, laser_c = Pipe()
    stream_p, stream_c = Pipe()
    iridium = Iridium()
    laser = Laser()

    timekeeper = Process(target=clock, args=(t,))
    broadcast = Process(target=iridium.broadcast)
    transmission = Process(target=iridium.image_transmission, args=(stream_p,))
    imaging = Process(target=capture_picture, args=(stream_c,))
    laser_list = Process(target=laser.measure, args=(laser_c, t,))

    timekeeper.start()
    broadcast.start()
    sleep(20)
    imaging.start()
    sleep(20)
    transmission.start()
	sleep(103)
	laser_list.start()
    sleep(768)
    broadcast.terminate()
    
    sleep(65)


    while 1:
        file.write("The iridium started sending at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')
        iridium.send_message(laser_p.recv())
        file.write("The iridium stopped sending at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')

if __name__ == '__main__':
    main()
