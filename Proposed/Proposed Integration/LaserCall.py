import time
import minimalmodbus as mini

class laser:
    mini.BAUDRATE=115200
    mini.PARITY='1'
    masterTime = time.strftime('%H:%M:%S')

    primaryInstrument = mini.instrument("/dev/ttyUSB1",1,mode='rtu')
    secondaryInstrument = mini.instrument("/dev/ttyUSB2",2,mode='rtu')

    def __init__(self):
        self.primaryInstance = ""
        self.secondaryInstance = ""
    def measure(self):
        primaryPass = primaryInstrument.read_register(24, functioncode = 4)
        secondaryPass = secondaryInstrument.read_register(24, functioncode = 4)

        if primaryPass < 1000:
            primaryInstance = ('Instance occurred at: {}'.format(masterTime))
            time.sleep(.5)
        if secondaryPass < 1000:
            secondaryInstance = ('Instance occurred at: {}'.format(masterTime))
            time.sleep(.5)

        combinedInstance = '{}|{}'.format(primaryInstance,secondaryInstance)
        return combinedInstance

    def temperature(self):
        primaryTemp = primaryInstrument.read_register(22,numberOfDecimals=2,functioncode=4)
        secondaryTemp = secondaryInstrument.read_register(22,numberOfDecimals=2,functioncode=4)

        primaryTemp = primaryTemp*(9/5)+32
        seondaryTemp = secondaryTemp*(9/5)+32

        combinedTemp = '{}|{}'.format(primaryTemp,secondaryTemp)
        return combinedTemp
