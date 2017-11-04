import time from timer
import strftime from time
import datetime
import os
import RPi.GPIO as GPIO
import minmialmodbus

instrument1results = "/results/instrument1results.txt"
instrument2results = "/results/instrument2results.txt"
instrument3results = "/results/instrument3results.txt"
masterCopy = "/results/masterCopyLog.txt"
#The one above gives a master list of all imporntnat times that happen.

instrument1 = minimalmodbus.instrument(#'GPIO port that lasers is associated too'# ,  #then the slave address(should be 0)#)
instrument2 = minimalmodbus.instrument(#'GPIO port that lasers is associated too'# ,  #then the slave address(should be 0)#)
instrument3 = minimalmodbus.instrument(#'GPIO port that lasers is associated too'# ,  #then the slave address(should be 0)#)
time = time.strftime('%H:%M:%S')
#time2 = time.time(start)
#timeEnd = time.time(start) + 900
#Time above outputs startime then adds 15 minutes to it so that it isnt an ifinite loop in theory still working this out.
distance1 = instrument1.read_register()
distance2 = instrument2.read_register()
distance3 = instrument3.read_register()

file1 = open(instrument1results, "w")
file1.write("Started recording at: " + time + '\n')
file2 = open(instrument2results, "w")
file2.write("Started recording at: " + time + '\n')
file3 = open(instrument3results, "w")
file3.write("Started recording at: " + time + '\n')
file4 = open(masterCopy, "w")
file4.write("Started laser recording at: " + time + '\n')
time.sleep(0.25)#lets the cpu rest for a second to prevent overheating

while time2 > 0 #we need to find a way to stop the program using time.
	if distance1 > 0:
		file1 = open(instrument1results, "w")
		file1.write("Instance occured at: " + time + '\n')
		file1.write(distance1)
		file4 = open(masterCopy, "w")
		file4.write("Instance occured at:" + time + '\n')
		file4.write(distance1)
	elif distance1 == 0:
		file1.write("Nothing is in the first lasers range." + '\n')
		file4.write("Nothing is in the first lasers range." + '\n')
	
	if distance2 > 0:
		file2 = open(instrument2results, "w")
		file2.write("Instance occured at: " + time + '\n')
		file2.write(distance2)
		file4 = open(masterCopy, "w")
		file4.write("Instance occured at: " + time + '\n')
		file4.write(distnace2)
	elif distance2 == 0:
		file2.write("Nothing is in the first lasers range." + '\n')
		file4.write("Nothing is in the first lasers range." + '\n')
	
	if distance3 > 0:
		file3 = open(instrument3resultsresults, "w")
		file3.write("Instance occured at: " + time + '\n')
		file3.write(distance3)
		file4 = open(masterCopy, "w")
		file4.write("Instance occured at: " + time + '\n')
		file4.write(distnace3)
	elif distance3 == 0:
		file3.write("Nothing is in the first lasers range." + '\n')
		file4.write("Nothing is in the first lasers range." + '\n')
			
			
#notes: their is many ways we can do this we could slpit into 3 files, one for each laser or we could do multiple whiles
# The most imporntnat thing we need to figure out right now is how to end the while loop if at all.
	
	
	
#Yes we should end the while loop eventually or we might get gibberish. We cou;d try dictionary mapping or classes? 
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
