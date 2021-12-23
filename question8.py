# Copy contents from one file to another file in Python


file_to_read="ReadData.txt"
write_to_file="WriteData.txt"

file = open(file_to_read,"r")
data = file.read()
file.close()


with open(write_to_file,"a") as file:
    file.write(data)
print("completed")
