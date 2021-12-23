# importing os library
import os

def main():
    # creating a new directory
    os.mkdir("pythonFiles3")

    # Changing current path to the directory
    os.chdir("pythonFiles3")

    # creating a new file for writing operation
    fo = open("test.txt","w")
    fo.write("This is demo File")
    fo.close()

    # printing the current file directory
    print("Current Directory :",os.getcwd())
    
if __name__=="__main__":main()

