from time import sleep
import serial

ser = serial.Serial(port="/dev/ttyUSB0", baudrate=19200, xonxoff=True)
x = 0
y = 0
while x != 10: 
    sleep(1)
    ser.write("AT+SBDWT=[TEST    ]\r".encode())
    p = ser.read(size=ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
    print(p)
    x += 1
    sleep(2)
 
	sleep(1)
	ser.write('AT+SBDIX\r'.encode())
	p = ser.read(size=ser.in_waiting).decode().translate(str.maketrans( '', '', ',')).split(" ")
	print(p)
	
	sleep(2)
	ser.write('AT+SBDD0\r'.encode())
	p = ser.read(size=ser.in_waiting).decode().translate(str.maketrans( '', '', ',')).split(" ")
	
	sleep(1)

ser.write("AT+SBDWT=[TEST    ]\r".encode())
p = ser.read(size=ser.in_waiting).decode().translate(str.maketrans( '', '', '')).split(" ")
sleep(1)
print(p)
ser.write('AT+SBDIX\r'.encode())
p = ser.read(size=ser.in_waiting).decode().translate(str.maketrans( '', '', ',')).split(" ")
print(p)
sleep(2)
ser.write('AT+SBDD0\r'.encode())
p = ser.read(size=ser.in_waiting).decode().translate(str.maketrans( '', '', ',')).split(" ")