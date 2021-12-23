# Python program to read data from file and extract record data from it.



# program to read data and extract records 
# from it in python

# Opening file in read format
File = open('flow.dat',"r")
if(File == None):
    print("File Not Found..")
else:
    while(True):
        # extracting data from records 
        record = File.readline()
        if (record == ''): break
        data = record.split(',')
        data[3] = data[3].strip('\n')
        
        # printing each record's data in organised form
        print('Code:',data[0])
        print('Name:', data[1])
        print('learn:', data[2])
        print('City:', data[3])
