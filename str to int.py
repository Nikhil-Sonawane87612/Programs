import csv
total_inventory_value=0
with open("test.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        price = float(row["Price"])
        quantity = int(row["Quantity"])
        total_inventory_value += price * quantity   
print(f"Total Stock Value: ₹{total_inventory_value:.2f}")