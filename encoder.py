from io import BytesIO, StringIO
from PIL import Image as IM
import base64
import numpy as np
from time import perf_counter


im1 = r'C:\Users\91868\Desktop\test1.png'
im2 = r'C:\Users\91868\Desktop\test2.png'
im3 = r'C:\Users\91868\Desktop\test3.png'

imd = r'C:\Users\91868\Desktop\small.jpg'

n1 = r'C:\Users\91868\Desktop\v1.png'

def crypt(message):
    new_message=""
    for e in message:
      if ord(e)<254:
          new_message+=chr(ord(e)+1)
      else:
          new_message += chr(ord(e))
    return new_message

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


m1="""
This is an era of wireless communication networks. People share their data to each other over world.
"""
m2="""
Hemant malik's Message: This is an era of wireless communication networks. People share their data to each other over the internet 
using different protocols like Http/Https, web sockets, FTP, SMTP etc. For the security of data cryptography 
plays an important role. With the increase in usages of the internet the cyber-attacks have also increased over 
the past few years. Thus, this problem gives rise to steganography techniques i.e. some advanced secret sharing 
techniques are evolved to hide a
"""
m3= """
Hemant malik's Message: This is an era of wireless communication networks. People share their data to each other over the internet 
using different protocols like Http/Https, web sockets, FTP, SMTP etc. For the security of data cryptography 
plays an important role. With the increase in usages of the internet the cyber-attacks have also increased over 
the past few years. Thus, this problem gives rise to steganography techniques i.e. some advanced secret sharing 
techniques are evolved to hide data in other files after applying cryptography to the confidential/secret data. 
This paper speaks about the different existing   techniques in cloud environments.
plays an important role. With the increase in usages of the internet the cyber-attacks have also increased over 
 past few years. Thus, this problem gives rise to steganography techniques i.e. some advanced secret sharing 
techniques are evolved to hide data in other files after applying cryptography to the confidential/secret data. 
"""

m4="""
Hemant malik's Message: This is an era of wireless communication networks. People share their data to each other over the internet 
using different protocols like Http/Https, web sockets, FTP, SMTP etc. For the security of data cryptography 
plays an important role. With the increase in usages of the internet the cyber-attacks have also increased over 
the past few years. Thus, this problem gives rise to steganography techniques i.e. some advanced secret sharing 
techniques are evolved to hide data in other files after applying cryptography to the confidential/secret data. 
This paper speaks about the different existing   techniques in cloud environments.
plays an important role. With the increase in usages of the internet the cyber-attacks have also increased over 
 past few years. Thus, this problem gives rise to steganography techniques i.e. some advanced secret sharing 
techniques are evolved to hide data in other files after applying cryptography to the confidential/secret data. 
Hemant malik's Message: This is an era of wireless communication networks. People share their data to each other over the internet 
using different protocols like Http/Https, web sockets, FTP, SMTP etc. For the security of data cryptography 
plays an important role. With the increase in usages of the internet the cyber-attacks have also increased over 
the past few years. Thus, this problem gives rise to steganography techniques i.e. some advanced secret sharing 
techniques are evolved to hide data in other files after applying cryptography to the confidential/secret data. 
This paper speaks about the different existing   techniques in cloud environments.
plays an important role. With the increase in usages of the internet the cyber-attacks have also increased over 
 past few years. Thus, this problem gives rise to steganography techniques i.e. some advanced secret sharing 
techniques are evolved to hide data in other files after applying cryptography to the confidential/secret data. 
Hemant malik's Message: This is an era of wireless communication networks. People share their data to each other over the internet 
using different protocols like Http/Https, web sockets, FTP, SMTP etc. For the security of data cryptography 
plays an important role. With the increase in usages of the internet the cyber-attacks have also increased over 
the past few years. Thus, this problem gives rise to steganography techniques i.e. some advanced secret sharing 
techniques are evolved to hide data in other files after applying cryptography to the confidential/secret data. 
This paper speaks about the different existing   techniques in cloud environments.
plays an important role. With the increase in usages of the internet the cyber-attacks have also increased over 
 past few years. Thus, this problem gives rise to steganography techniques i.e. some advanced secret sharing 
techniques are evolved to hide data in other files after applying cryptography to the confidential/secret data. 
Hemant malik's Message: This is an era of wireless communication networks. People share their data to each other over the internet 
using different protocols like Http/Https, web sockets, FTP, SMTP etc. For the security of data cryptography 
plays an important role. With the increase in usages of the internet the cyber-attacks have also increased over 
the past few years. Thus, this problem gives rise to steganography techniques i.e. some advanced secret sharing 
techniques are evolved to hide data in other files after applying cryptography to the confidential/secret data. 
This paper speaks about the different existing   techniques in cloud environments.
plays an important role. With the increase in usages of the internet the cyber-attacks have also increased over 
 past few years. Thus, this problem gives rise to steganography techniques i.e. some advanced secret sharing 
techniques are evolved to hide data in other files after applying cryptography to the confidential/secret data. 
Hemant malik's Message: This is an era of wireless communication networks. People share their data to each other over the internet 
using different protocols like Http/Https, web sockets, FTP, SMTP etc. For the security of data cryptography 
plays an important role. With the increase in usages of the internet the cyber-attacks have also increased over 
the past few years. Thus, this problem gives rise to steganography techniques i.e. some advanced secret sharing 
techniques are evolved to hide data in other files after applying cryptography to the confidential/secret data. 
This paper speaks about the different existing   techniques in cloud environments.
plays an important role. With the increase in usages of the internet the cyber-attacks have also increased over 
 past few years. Thus, this problem gives rise to steganography techniques i.e. some advanced secret sharing 
techniques are evolved to hide data in other files after applying cryptography to the confidential/secret data. 

"""
start = perf_counter()
msg = encoder3(im3, m4, n1)
end = perf_counter()
print('Message Length:',len(m4),'\nEncoding time:', round(end - start,3))







