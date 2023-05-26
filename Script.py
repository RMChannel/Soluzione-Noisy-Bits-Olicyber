from PIL import Image
import string
import re
import os
file=Image.open("bits.bmp")
file=str(file.tobytes())
file=file.replace("x00","0")
file=file.replace("xff","1")
chars = re.escape(string.punctuation)
file=re.sub('['+chars+']', '',file)
file=file[1:]
listofbin=[]
i2=0
temp=""
for i in file:
    temp=temp+i
    i2+=1
    if i2==8:
        temp=int(temp,2)
        listofbin.append(temp)
        temp=""
        i2=0
listofbin=bytearray(listofbin)
print(listofbin)
file2=open("output.zip","wb")
file2.write(listofbin)