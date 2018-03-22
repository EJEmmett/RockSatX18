#takes the error code and gives us the message that goes along with it
#Written by: Samuel Schatz for RockSat2018
#meant to be added  


from random import *#these two lines work as the error message number
num = randint(0, 65)
errorArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 64, 65, 66]

v1 = "3"
v2 = "14"
v3 = "20"
v4 = "32"
v5 = "39"
v6 = "63"

errorArray[0] = "No error."
errorArray[1]= "Auto-registration has been performed successfully (mode 1 only)."
errorArray[2] = "Session completed but the requested Location Update was not accepted."
if num >= 3 and num <= 14:
    errorArray[4] = "Passive Geolocation was performed and the SSD is attached to the gateway, but the SSD location has not changed enough to require a new registration"
    num = 4
errorArray[15] = "Access is denied."
errorArray[16] = "ISU has been locked and may not make SBD calls"
errorArray[17] = "Gateway not responding (local session timeout)."
errorArray[18] = "Connection lost (RF drop)." 
errorArray[19] = "Link failure (A protocol error caused termination of the call)." 
if num >= 20 and num <= 32:
    errorArray[27] = "Reserved, but indicate failure if used." 
    num = 27
errorArray[32] = "No network service, unable to initiate call." 
errorArray[33] = "Antenna fault, unable to initiate call." 
errorArray[34] = "Radio is disabled, unable to initiate call (see *Rn command)." 
errorArray[35] = "ISU is busy, unable to initiate call." 
errorArray[36] = "Try later, must wait 3 minutes since last registration." 
errorArray[37] = "SBD service is temporarily disabled." 
errorArray[38] = "Try later, traffic management period (see +SBDLOE command)" 
if num >= 39 and num <= 63:	
    errorArray[46] = "Reserved, but indicate failure if used." 
    num = 46
errorArray[64] = "Band violation (attempt to transmit outside permitted frequency band)." 
errorArray[65] = "PLL lock failure; hardware error during attempted transmit." 

print(errorArray[num])

