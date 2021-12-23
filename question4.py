N = ["Be\n", "Happy\n", "Alone\n"]
 
# Writing to a file
file1 = open('test.txt', 'w')
file1.writelines((N))
file1.close()
 
# Using readline()
file1 = open('test.txt', 'r')
count = 0
 
while True:
    count += 1
 
    # Get next line from file
    line = file1.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    print("Line{}: {}".format(count, line.strip()))
 
file1.close()