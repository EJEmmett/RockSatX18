from time import sleep
from multiprocessing import Pipe, Process, Array
from functions import Iridium, capture_picture, clock, pic_for_sending

def main():
    file = open("/home/pi/masterLog.txt", "a+")
    t = Array("i", 2)
    laser_p = Pipe()
    iridium = Iridium()
    laser = Laser()

    print("started")
    timekeeper = Process(target=clock, args=(t,))
    broadcast = Process(target=iridium.broadcast)
    image_transmission = Process(target=iridium.image_transmission)
    registration = Process(target=iridium.register)

    imaging = Process(target=capture_picture)
	imaging2 = Process(target= pic_for_sending)

    timekeeper.start()
    sleep(26)
    registration.start()
    file.write("The iridium started registering at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')
    sleep(1)
    registration.terminate()
    sleep(9)
    file.write("The iridium stopped registering at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')
    broadcast.start()
    file.write("The iridium started broadcasting at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')
    sleep(10)
	imaging.start()
	sleep(49)
	imaging2.start()
	sleep(1)
	imaging2.terminate()
    broadcast.terminate()
	image_transmission.start()
    file.write("The iridium stopped broadcasting at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n'
    sleep(60)
    file.write("The iridium started sending the pictures at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')
    sleep(649)
    image_transmission.terminate()
    file.write("The iridium stopped sending the pictures at: " + str(t[0]).zfill(2)+":"+str(t[1]).zfill(2) + '\n')

main()
