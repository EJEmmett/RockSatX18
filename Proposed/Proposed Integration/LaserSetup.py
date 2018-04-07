import serial
from LaserCall import laser
ser = serial.Serial(port='/dev/ttyUSB2')
l = laser()

while 1:
    sendmessage(l.measure())

def sendMessage(m):
    ser.write('AT')
    if ser.inWaiting()>0:
        ser.write('AT+SDBWRT({})\r\n'.format(m))
        time.sleep(1)
        ser.write('AT+SBDIX\r\n')
        while ser.inWaiting()>0:
            out += ser.read(1)
