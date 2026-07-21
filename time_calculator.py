def calculate_focus_time(commute_hours, college_hours, sleep_hours):
    available_time = 24 - (commute_hours + college_hours + sleep_hours)
    return available_time

available_time = calculate_focus_time(5, 8, 8)

if available_time>=2:
    print("Success")
else:
    print("Warning")
    
calculate_focus_time(5, 8, 8)
