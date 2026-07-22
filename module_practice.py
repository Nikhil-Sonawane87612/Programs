import random
import datetime

print(datetime.datetime.now())

status=["SERVER_OK","HIGH_LATENCY","DATABASE_SYNCED"]
a=random.choice(status)
log=f" TimeStamp: {datetime.datetime.now()} \t Status: {a} \n-------------------"

try :
    with (open("system_status.log", "a")) as file:
        file.write(log)
    print("Succefully Log Created")
    print(log)
except Exception as e:
    print(f"Failed to generate log {e}")
