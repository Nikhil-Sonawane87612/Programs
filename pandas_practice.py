import pandas as pd
sales_data = {
    "Employee": ["Nikhil", "Amit", "Suresh", "Neha"],
    "Sales": [150000, 85000, 120000, 95000],
    "Region": ["West", "North", "West", "East"]
}

df=pd.DataFrame(sales_data)
print(df)
# CORRECT
total = df["Sales"].sum()    # Calculates sum: 450000
average = df["Sales"].mean()  # Calculates average: 112500.0
print(f"Total Sales : {total}")
print(f"Average Sales : {average}")
region_west= (df[df["Region"] == "West"])

print(region_west)