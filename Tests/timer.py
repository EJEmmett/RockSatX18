from time import sleep
from timeit import default_timer as timer

class Clock:
    def __init__(self):
        self.second = 0
        self.minute = 0

    def increment(self, n):
        while 1:
            self.second+=1
            if self.second == 60:
                self.minute+=1
                self.second = 0
            n[0] = self.minute
            n[1] = self.second
            sleep(1)
