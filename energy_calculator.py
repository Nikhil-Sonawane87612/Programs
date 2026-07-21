def calculate_energy_stamina(commute_hours,sleep_hours):
    available_energy=100-(commute_hours*10)-((8-sleep_hours)*15)
    return max(available_energy,0)

my_energy = calculate_energy_stamina(commute_hours=5, sleep_hours=7)
print(f"Projected Focus Energy: {my_energy}%")