import serial
from LaserCall import laser
from time import sleep

ser = serial.Serial(port='/dev/ttyUSB0',19200)
l = laser()
out = ""

while 1:
    
    if l.measure():
        sendmessage(l.measure())
        
    ser.reset_output_buffer()


def sendMessage(m):
    ser.write('AT')
    
    if ser.inWaiting()>0:
        ser.write('AT+SDBWRT({})\r\n'.format(m).encode('utf-8'))
        sleep(1)
        ser.write('AT+SBDIX\r\n'.encode('utf-8'))
        
        if ser.in_waiting!=0:
            ser.reset_input_buffer()
