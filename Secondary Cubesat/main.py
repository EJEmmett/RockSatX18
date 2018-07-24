from time import sleep
import serial

def main():
    x = 0
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=19200, xonxoff=True)
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    sleep(69)
    while x != 5:
        ser.write(b'AT+SBDREG')
        x = x + 1
    while True:
        ser.write('AT+SBDWT=Major Tom to ground control                   \r'.encode())
        sleep(.1)
        ser.write('AT+SBDIX\r'.encode())
        sleep(2)
        ser.write('AT+SBDD0\r'.encode())
        sleep(.1)

main()
