#Use open()  , write() to write data into file and it'll create new test.txt if not exist or overwrite if present
with open ("test.txt", 'w') as file:
    file.write("Day 3 : File Handling Started \n ")
# Adds a new line at the very bottom without deleting old lines
with open("test.txt", "a") as file:
    file.write("Day 3 : Appending/Adds new Content to File")
    
# Reads the entire content as text
with open("test.txt", "r") as file:
    content=file.read()
    print(content)