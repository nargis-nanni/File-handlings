# Python program to check a file's status in file Handling.

# Program to check a file's status in file Handling...

# main method 
def main():
    # Opening the file 
    fileObject = open("low.dat","rb")

    # Printing object's status
    print("Name of the File : ",fileObject.name)
    print("Closed or Not    : ",fileObject.closed)
    print("Opening Mode     : ",fileObject.mode)

    fileObject.close()

    print("")
    print("Closed or Not    : ",fileObject.closed)

if __name__=="__main__":main()