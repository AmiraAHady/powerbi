x=5
y=12

def printx():
    print(x)
    
printx() 

with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a sample text file.\n")  


with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)
    
with open("example.txt", "a") as file:
    file.write("Adding another line.\n")

# 4. Read again to see the update
with open("example.txt", "r") as file:
    print("Updated content:")
    print(file.read())        

 