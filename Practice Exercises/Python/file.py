file_path="C:/Users/USER/Documents/example.txt"

with open(file_path,"w") as file:
    file.write("Hello, this content is written to a file in your laptop")

print("File created and content written successfully")

with open("C:/Users/USER/Documents/example.txt",'r') as file:
    for line in file:
        print(line.strip())

with open("C:/Users/USER/Documents/example.txt",'a') as file:
    file.write("\nThis is the second line that is appended")

with open("C:/Users/USER/Documents/example.txt","r") as file:
    content = file.read()
    print(content)