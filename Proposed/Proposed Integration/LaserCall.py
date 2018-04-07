import time
import minmialmodbus as mini

class laser:
    Switch = False
    masterTime = time.strftime('%H:%M:%S')

    primaryInstrument = mini.instrument("/dev/ttyUSB0")
    secondaryInstrument = mini.instrument("/dev/ttyUSB1")
    primaryPass = primaryInstrument.read_register()
    secondaryPass = secondaryInstrument.read_register()

    def __init__(self):
        self.primaryInstance = ""
        self.secondaryInstance = ""
    def measure(self):
        if primaryPass != 0:
            primaryInstance = (f"Instance occurred at: {masterTime}")
            time.sleep(1)
        if secondaryPass != 0:
            secondaryInstance = (f"Instance occurred at: {masterTime}")
            time.sleep(1)

        combinedInstance = f"{primaryInstance}|{secondaryInstance}"
        return combinedInstance
