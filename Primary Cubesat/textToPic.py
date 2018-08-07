import base64
from time import sleep

with open("/home/sam/Downloads/SBD/picBASE64.txt") as f:
    c1 = f.readline(1)
    c1 = c1[:-2]
    c2 = f.readline(2)
    c2 = c2[:-2]
    c3 = f.readline(3)
    c3 = c3[:-2]
    c4 = f.readline(4)
    c4 = c4[:-2]
    c5 = f.readline(5)
    c5 = c5[:-2]
    c6 = f.readline(6)
    c6 = c6[:-2]
    c7 = f.readline(7)
    c7 = c7[:-2]
    c8 = f.readline(8)
    c8 = c8[:-2]
    c9 = f.readline(9)
    c9 = c9[:-2]
    c10 = f.readline(10)
    c10 = c10[:-2]
    c11 = f.readline(11)
    c11 = c11[:-2]
    c12 = f.readline(12)
    c12 = c12[:-2]
    c13 = f.readline(13)
    c13 = c13[:-2]
    c14 = f.readline(14)
    c14 = c14[:-2]
    c15 = f.readline(15)
    c15 = c15[:-2]
    c16 = f.readline(16)
    c16 = c16[:-2]
    c17 = f.readline(17)
    c17 = c17[:-2]

        
c = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10
c = c + c11 + c12 + c13 + c14 + c15 + c16 + c17 + c18 + c19 + c20
c = c + c21 + c22 + c23 + c24 + c25 + c26 + c27
c = base64.b64decode(c)
with open("/home/sam/Downloads/pic.jpg", "w") as pic:
        pic.write(c)
        pic.close()
        f.close()
        
        
        
        
        
        
