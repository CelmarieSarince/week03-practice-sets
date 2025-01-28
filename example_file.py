# Open a file in read mode ('r')
# Open a file in write mode ('w')
#with open('example.txt', 'w') as file:
    #file.write("This is a new file.\n")
    #file.write("File handling in Python is simple!\n")
#print("File written successfully!")

# Open a file in read mode ('r')
#with open('example.txt', 'r') as file:
    #content = file.read()
    #print("File Content:\n", content)

# Open a file and read line by line
#with open('example.txt', 'r') as file:
    #for line in file:
        #print(line.strip())  # `strip()` removes trailing newlines

try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found! Please check the file name.")
