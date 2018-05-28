from datetime import datetime
import minimalmodbus as mini

class Laser:
    def __init__(self, port):
        mini.BAUDRATE=115200
        self.primaryInstrument = mini.Instrument(port, 1, mode='rtu')
        self.primaryInstrument.write_register(4, value=20, functioncode=6)

    def measure(self,q):
        primaryPass = self.primaryInstrument.read_register(24, functioncode = 4)
        instance = None

        if primaryPass is not 0:
            instance = ('Laser passed at: ' + datetime.now().strftime('%H:%M:%S'))

        if instance is not None:
            with open("masterLog.txt", "a") as f:
                f.write(instance+"\n")
            q.put(instance)
