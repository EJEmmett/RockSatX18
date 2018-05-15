from time import sleep
import serial

def main():
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=19200, xonxoff=True)
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    while True:
        ser.write('AT+SBDWRT=Hello World'.encode())
        sleep(.1)
        ser.write('AT+SBDIX\r'.encode())
        sleep(.1)
        ser.reset_input_buffer()
        ser.reset_output_buffer()

main()
