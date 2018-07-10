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
	laser_broadcast = Process(target=iridium.send_message, args=(laser_p.recv(),))
	
    timekeeper.start()
	sleep(5)
    broadcast.start()
	file.write("The iridium started sending at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')
    sleep(20)
    imaging.start()
	file.write("The imaging started at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')
    sleep(20)
    transmission.start()
	file.write("The iridium started sending the pictures at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')
	sleep(125)
	laser_list.start()
	file.write("The lasers started at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')
	laser_broadcast.start()
	file.write("The iridium started sending at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')
	sleep(60)
	laser_broadcast.stop()
	file.write("The iridium started sending at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')
    sleep(768)
	transmission.start()
	file.write("The iridium started sending the pictures at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')
    broadcast.terminate()
    
    sleep(65)


    while 1:
        file.write("The iridium started sending at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')
        iridium.send_message(laser_p.recv())
        file.write("The iridium stopped sending at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')

if __name__ == '__main__':
    main()
