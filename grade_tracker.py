subject_score={
    "Python":88,
    "DBMS": 75,
    "Networking": 82
}

score_list=subject_score.values()
total_score=sum(subject_score.values())
avg_score= total_score/len(subject_score)

for subject,score in subject_score.items():
    print(f"Subject {subject} : {score} marks")
print(f"Average Marks : {avg_score}")