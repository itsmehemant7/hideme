from io import BytesIO, StringIO
from PIL import Image as IM
import base64
import numpy as np
from time import perf_counter

#Below these 3 are sample (512*512) input images

im1 = r'C:\Users\91868\Desktop\test1.png'
im2 = r'C:\Users\91868\Desktop\test2.png'
im3 = r'C:\Users\91868\Desktop\test3.png'

n1 = r'C:\Users\91868\Desktop\v1.png'   #This is the path for output image named v1


def crypt(message):
    # cryptography
    message=message.replace('a',"@")
    message=message.replace('e','#') 
    message=message.replace('i',"*")
    return message

"""
The crypt() function is just a demo for symmetric key cryptography.
For more security change the message into base64 string and then embed it in image after applying cryptography.
"""

def encoder3(image, message, path):
    message = crypt(message)
    msg = message.encode('ascii')
    msg = msg + b'xxxxxx'
    mlist = []
    a = ""
    b = ""
    c = ""
    j=0
    while(j<len(msg)):
        a = msg[j]
        try:
           b = msg[j+1]
           c = msg[j+2]
        except:
            b=34
            c=34
        j=j+3
        mlist.append((a, b, c))

    img = IM.open(image)
    width, height = img.size
    pixels = img.load()
    new = IM.new('RGB', (width, height))
    pix = new.load()
    count = 0
    for e in range(width):
        for a in range(height):
            if e == 0 or e == 1 or e == 2 or e == 3:
                if count < len(mlist):
                    pix[e, a] = mlist[count]
                    count = count + 1
                else:
                    pix[e, a] = pixels[e, a]
            else:
                pix[e, a] = pixels[e, a]
    new.save(path)
    return msg


msg="""
This is our sample message for hiding. This will be encrypted first and then embeded into image.
You can vary or change this message if you wants to.
"""

start = perf_counter()
msg = encoder3(im1, msg, n1)
end = perf_counter()

print('Message Length:',len(msg),'\nEncoding time:', round(end - start,3))


"""
Message length and time taken for encryption are the 2 outputs of this program.

The Output stego image will be stored at path given (i.e 'n1' here).
This stego image will act as the input for decryptor.
"""







