
try:
    file=open("Exception_handling.txt","r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Warning: Log file not found! Creating a new one...")
    with open("Exception_handling.txt", "w") as file:
        file.write("Initial log entry.")
    print("Log file created.")