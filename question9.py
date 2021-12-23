# Copy odd lines of one file to another file in Python

f=open("file.txt","r")
f1=open("file.txt","w")
count=1
for i in f:
    if count%2!=0:
        f1.write(i)
    count+=1    
