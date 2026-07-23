import pandas as pd
data={
    "Student": ["Nikhil ", "Rohit", "Sakshi", "Anjali"],
    "Score": [85, 90, 78, 92],
    "Attendance": [98,80,92,75]
}

df=pd.DataFrame(data)   

print("--- Full DataFrame--- ")
print(df)\

print("--- Quick Stats ---")
print(f"Average Score : {df['Score'].mean()}")
print(f"Maximum Score: {df['Score'].max()}")

passed_students= df[df['Score']>=75]
print("--- Passed Students ---")
print (f" {passed_students}")


df= pd.read_csv("marks.csv")
df["Passed"]= df['Score'] >=40
df.to_csv("updated_student.csv",index=False)

print("Updated CSV saved with 'Passed' status column!")
print(df)


