from io import BytesIO, StringIO
from PIL import Image as IM
import base64
import numpy as np
from time import perf_counter

n1 = r'C:\Users\91868\Desktop\v1.png'

def decrypt(message):
    #cryptography
    message = message.replace('@', "a")
    message = message.replace('#', 'e')
    message = message.replace('*', "i")
    return message


def decoder3(image):
    img=IM.open(image)
    width,height=img.size
    pixels=img.load()
    mlist=[]
    for e in range(width):
        for a in range(height):
            if e == 0 or e == 1 or e == 2 or e == 3:
                mlist.append(pixels[e,a])
            if e > 3:
                break
    s=""
    for e in mlist:
        s=s+chr(e[0])+chr(e[1])+chr(e[2])
    i=s.index('xxxxx')
    s=s[0:i]
    s=decrypt(s)  #cryptography
    return s
start = perf_counter()
d=decoder3(n1)
print(d)

end = perf_counter()
print('Message Length:',len(d),'\nDecoding time:', round(end - start,3))



"""
The output of this program will decoding time and the hidden message itself.
"""
