with open("my_journal.txt", "w") as file:
    file.write("Nikhil Sonawane : 3rd year BCA Student \n")

with open("my_journal.txt","a") as file:
    file.write("Day 3: Mastered file handling directly with JARVIS \n")

with open ("my_journal.txt", "r") as file:
    content=file.read()
    print(content)