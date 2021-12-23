# Python program to read character till a count

# Python program to read character till a count

# main function
def main():
    # opening the file in read mode.
    file = open("ill.dat","r")

    # printing file name 
    print("Name of the File : ",file.name)

    # reading 10 characers 
    String = file.read(10)
    print("Read String is till 10       : ",String)
    position = file.tell()
    print("Current Position             : ",position)
    String =file.read(10)
    print("Read String is till next 10  : ",String)
    position = file.tell()
    print("Current Position             : ",position)
    print()
    print("Sending Pointer back to Top")
    position = file.seek(0,0)
    print("Current Position             : ",position)
    String =file.read(25)
    print("Read String is till 25       : ",String)
    position = file.tell()
    print("Current Position             : ",position)

    file.close()

if __name__=="__main__":main()