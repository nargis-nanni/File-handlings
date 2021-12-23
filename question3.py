
# Python program to illustrate
# Append vs write mode
file1 = open("test.txt","w")
L = ["I am nargis \n","my nick name is nunny \n","I love python \n"] 
file1.writelines(L)
file1.close()
  
# Append-adds at last
file1 = open("test.txt","a")#append mode
file1.write("Today \n")
file1.close()
  
file1 = open("test.txt","r")
print("Output of Readlines after appending") 
print(file1.readlines())
print()
file1.close()
  
# Write-Overwrites
file1 = open("test.txt","w")#write mode
file1.write("Now I am learningS \n")
file1.close()
  
file1 = open("Demo.txt","r")
print("Output of Readlines after writing") 
print(file1.readlines())
print()
file1.close()