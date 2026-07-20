travel_time= int (input("Enter the travel time in hours: "))
energy_level= int(input("Enter the energy level as a 0-10: "))
if travel_time >4 and energy_level <5:
    print("Critical Fatigue Risk. Stick to low-energy audio learning on the commute today.")
elif travel_time >4 and energy_level >=5:
    print("High stamina maintained. Optimize the travel block for deep conceptual mapping.")
else:
    print("Standard operational day. Maximize home focus block.")
