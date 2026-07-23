import json 
config={
    "appname": "Jarvis CLI",
    "theme": "Dark",
    "max_threads": 4,
    "features" : ["AutoSync", "Error Logging", "Git Sync"]
}

with open("app_settings.json", "w") as file:
    json.dump(config, file , indent=4)
print("Created app_settings.json successfully!")


with open("app_settings.json", "r") as file:
    Data = json.load(file)

print("Current App Settings:")
print(f"App Name : {Data['appname']} and Theme : {Data['theme']}")
print(f"\n Count of Active Features : {len(Data['features'])}")