import serial
from LaserClass import Lasers
from time import sleep

ser = serial.Serial(port='/dev/ttyUSB0',19200)

def sendMessage(m):
    ser.write('AT+')
    if ser.out_waiting!=0:
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        ser.write('AT+SDBWRT({})\r\n'.format(m).encode('utf-8'))
        sleep(1)
        ser.write('AT+SBDIX\r\n'.encode('utf-8'))
        if ser.out_waiting!=0:
            ser.reset_input_buffer()
            ser.reset_output_buffer()

with Lasers() as l:
    while 1:
        if l.measure():
            sendMessage(l.measure())
