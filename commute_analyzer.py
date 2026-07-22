weekly_commute=[5.0, 4.5, 5.2, 4.8, 5.0]
total_hours=sum(weekly_commute)
avg_hours= total_hours / len(weekly_commute)
day_num=1
for time in weekly_commute:
    print(f"Day : {day_num} : {time} hours ")
    day_num +=1
print(f"Total Travel this Week : {total_hours}")
print(f"Average Travel this Week : {avg_hours}")
print(f"Longest Day : {max(weekly_commute)} hours")