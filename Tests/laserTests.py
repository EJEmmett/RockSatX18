import timeit
from datetime import datetime

def rep():
    #String replacement - 0.2546598883185716 seconds
    i = ('Laser 1 passed at: {}'.format("12:24:11"))

def con():
    #String concatnation
    i = ('Laser 1 passed at: ' + "12:24:11")

def averages(rep1, con1):
    a=0
    b=0

    for num in rep1:
        a += num

    for num in con1:
        b += num

    average1 = (a/100)
    average2 = (b/100)
    print(average1)
    print(average2)

#rep1 = timeit.repeat(rep, repeat=100)
#con1 = timeit.repeat(con, repeat=100)

#averages(rep1, con1)
