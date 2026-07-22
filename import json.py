import json

# Create initial structure
user_profile = {
    "username": "Nikhil_Sonawane",
    "role": "BCA Developer",
    "skills": ["Python", "Git", "File I/O"],
    "active_streak_days": 4
}

# Write it to disk
with open("user_profile.json", "w") as file:
    json.dump(user_profile, file, indent=4)

print("Created user_profile.json successfully!")