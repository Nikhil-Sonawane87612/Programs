import csv

# --- STEP 1: WRITE TO CSV ---
with open("marks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Subject", "Score"])  # Clean header (no trailing space)
    writer.writerow(["Nikhil", "Python", 88])
    writer.writerow(["Rahul", "DBMS", 75])
    writer.writerow(["Priya", "Networking", 92])

# --- STEP 2: READ AND CALCULATE AVERAGE ---
total_score = 0
student_count = 0

with open("marks.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Move 'Marks'ṇ conversion INSIDE the loop so it runs for every row
        score = int(row["Score"])
        
        # Accumulate score and count
        total_score += score
        student_count += 1
        
        print(f"Name : {row['Name']} | Subject : {row['Subject']} | Score : {score}")

# Calculate average outside the loop after all rows are read
avg_score = total_score / student_count
print("----------------------------------------")
print(f"Total Average Score: {avg_score:.2f}")