#!/bin/bash

rm /home/pi/main.txt
tm /home/pi/mainLasers.txt

sleep(1)

touch /home/pi/main.txt
touch /home/pi/mainLasers.txt

mount #the location of the of the first laser
mount #the location of the of the second laser
mount #the location of the irdium

