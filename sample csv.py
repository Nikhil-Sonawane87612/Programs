import csv
with open("test.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Item", "Quantity", "Price"])
    writer.writerow(["Laptop", 5,55000])
    writer.writerow(["Mouse", 12, 600])
print("CSV file created successfully.")

with open("test.csv", "r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(f"Item: {row['Item']}, Quantity: {row['Quantity']}, Price: {row['Price']}")

print("CSV file read successfully.")