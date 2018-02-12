import time from timer
import strftime from time
import datetime
import os
import RPi.GPIO as GPIO
import minmialmodbus
from time import sleep

instrument1results = "/results/instrument1results.txt"
instrument2results = "/results/instrument2results.txt"
masterCopy = "/results/masterCopyLog.txt"
#The one above gives a master list of all imporntnat times that happen.

instrument1 = minimalmodbus.instrument(#'GPIO port that lasers is associated too'# ,  #then the slave address(should be 0)#)
instrument2 = minimalmodbus.instrument(#'GPIO port that lasers is associated too'# ,  #then the slave address(should be 0)#)
masterTime = time.strftime('%H:%M:%S')
startTime = time.strftime('%S')
endTime = time.strftime('%S')
#time2 = time.time(start)
#timeEnd = time.time(start) + 900
#Time above outputs startime then adds 15 minutes to it so that it isnt an ifinite loop in theory still working this out.
distance1 = instrument1.read_register()
distance2 = instrument2.read_register()

file1 = open(instrument1results, "w")
file1.write("Started recording at: " + masterTime + '\n')
file2 = open(instrument2results, "w")
file2.write("Started recording at: " + masterTime + '\n')
file3 = open(masterCopy, "w")
file3.write("Started laser recording at: " + masterTime + '\n')
time.sleep(0.25)#lets the cpu rest for a second to prevent overheating

while masterTime > 0 #we need to find a way to stop the program using time.
	if distance1 > 0:
		timeOfInstanceStart1 = startTime
		file1 = open(instrument1results, "w")
		file1.write("Instance occured at: " + masterTime + '\n')
		file1.write(distance1)
		file3 = open(masterCopy, "w")
		file3.write("Instance occured at: " + masterTime + '\n')
		file3.write(distance1)
		time.sleep(0.5)
	timeOfInstanceEnd1 = endTime
	timeSpeed1 = str(timeOfInstanceEnd1 - timeOfInstanceStart1)
	speed1 = str(distance1/timeSpeed1)
	file1.write("Total speed in meters per second: " + speed1 + " At " + masterTime+ '\n')
	file3.write("Total speed in meters per second for the first laser: " + speed1 + " At " + masterTime + '\n')
	elif distance1 == 0:
		file1.write("Nothing is in the first lasers range." + '\n')
		file3.write("Nothing is in the first lasers range." + '\n')

while masterTime > 0:
	if distance2 > 0:
		timeOfInstanceStart2 = startTime
		file2 = open(instrument2results, "w")
		file2.write("Instance occured at: " + masterTime + '\n')
		file2.write(distance2)
		file3 = open(masterCopy, "w")
		file3.write("Instance occured at: " + masterTime + '\n')
		file3.write(distnace2)
		time.sleep(0.5)
	timeOfInstanceEnd2 = endTime
	timeSpeed2 = str(timeOfInstanceEnd2 - timeOfInstanceStart2)
	speed2 = str(distance2 / timeSpeed2)
	file2.write("Total speed in meters per second: " + speed2 + " At " + masterTime+ '\n')
	file3.write("Total speed in meters per second for the second laser: " + speed2 + " At " + masterTime+ '\n')
	elif distance2 == 0:
		file2.write("Nothing is in the first lasers range." + '\n')
		file3.write("Nothing is in the first lasers range." + '\n')
		

#notes: their is many ways we can do this we could slpit into 3 files, one for each laser or we could do multiple whiles
#The most imporntnat thing we need to figure out right now is how to end the while loop if at all.
#Written by Samuel Schatz for Rock Sat 2018 Janus.			

	
	
#Yes we should end the while loop eventually or we might get gibberish. We could try dictionary mapping or classes? 
# I was looking for a switch statement but Python doesn't like those. 
#	Found something else. Think this could work? 
#	def zero():
 #   return "zero"

#def one():
 #   return "one"

#def numbers_to_functions_to_strings(argument):
   # switcher = {
      #  0: zero,
     #   1: one,
    #    2: lambda: "two",
   # }
    # Get the function from switcher dictionary
  #  func = switcher.get(argument, lambda: "nothing")
 #   # Execute the function
#    return func()
