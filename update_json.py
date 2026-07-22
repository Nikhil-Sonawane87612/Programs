import json

# 1. Load existing data
with open("user_profile.json", "r") as file:
    data = json.load(file)

# 2. Safely modify fields
data["active_streak_days"] += 1
data["skills"].append("JSON Handling")

# 3. Save back to disk
with open("user_profile.json", "w") as file:
    json.dump(data, file, indent=4)

print("Profile updated with new skills and streak day!")