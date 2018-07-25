from time import sleep
import serial

def main():
    x = 0
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=19200, xonxoff=True)
    ser.reset_input_buffer()
    ser.reset_output_buffer()
	o = open("/home/pi/masterLog.txt", "a+")
    sleep(69)
    while x != 5:
        ser.write(b'AT+SBDREG')
        x = x + 1
    while True:
        ser.write('AT+SBDWT=[BM1:Major Tom to ground control               ]\r'.encode())
		o.write("Began to beacan")
		o.close()
        sleep(.1)
        ser.write('AT+SBDIX\r'.encode())
		o.write("Sent beacan")
		o.close()
        sleep(2)
        ser.write('AT+SBDD0\r'.encode())
        sleep(.1)

main()
