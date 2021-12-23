# Python program to delay printing of lines from a file using sleep function

import time

F=open("txt.txt","r")

while(True):
    b=F.read(1)
    if(b==""):
        break
    print(b,end="")
    time.sleep(0.3)

F.close()