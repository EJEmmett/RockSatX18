import minimalmodbus as mini
from datetime import datetime

mini.BAUDRATE=115200
primaryInstrument = mini.Instrument(port, 1, mode='rtu')
primaryInstrument.write_register(4, value=20, functioncode=6)
o = open("masterLog.txt", "a+")

while 1:
    primaryPass = primaryInstrument.read_register(24, functioncode = 4)
    instance = None
    if primaryPass is not 0:
        instance = ('Laser passed at: ' + datetime.now().strftime('%H:%M:%S'))
    if instance is not None:
        #print(instance)
		o.write(instance)
