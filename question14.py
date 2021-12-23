# Python program to read first N character from each line.

# Program to read first N character 
# from each line in python 

import time

# Opening the file
File = open('file.dat','r')

while(True):
    # Reading line using readline()
    data = File.readline()
    if(data==''):break
    #  Printing only 2 character from each line 
    print(data[0:2],end=' ')
    time.sleep(0.3)

File.close()