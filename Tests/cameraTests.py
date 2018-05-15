import timeit
def rep():
    #String replacement
    pictureFileName = "pic#.jpg"
    outputVersion = 1
    pictureFileName1 = pictureFileName.replace("#", str(outputVersion))

def con():
    #String concatnation
    outputVersion = 1
    pictureFileName = "pic"+ str(outputVersion) +".jpg"

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

rep1 = timeit.repeat(rep, repeat=100)
con1 = timeit.repeat(con, repeat=100)

averages(rep1, con1)
