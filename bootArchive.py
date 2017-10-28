# This file is for assurance purposes and to help us see when the two pi's conect.
import socket
from time import gmtime, strftime
import os
import time

#If we decide to make sure the ip's are right then we need to run this code first.
#os.system("ifcofig eth0 ****.****.***.****")
bootFile = "root/Desktop/boot.txt" #This can change based on how we decied to make the file system.
bootFileVersion = 1
file = open(bootFile, "w")
file.write("The boot time was: " + time.strftime('%a %H:%M:%S %Y.') + '\n')
time.sleep(0.5)
os.systen("ping -c 1 127.0.0.1 >> boot.txt") #The IP address will be changed acourding to the pi's address.
file.write('\n' + "It worked!")

# once the syntax for the irdium network is found this part will sen this file.
