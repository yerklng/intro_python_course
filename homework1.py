# Task 1
day = input("Day when you were born: ")
month = input("Month when you were born: ")
year = input("Year when you were born: ")

print(f"{day}/{month}/{year}")

# Task 2
income = float(input("Your year's income: "))

if income < 10000:
    rate = 0.08
elif income <= 26000:
    rate = 0.12
else:
    rate = 0.24

tax = income * rate
print(f"Tax: {tax}")

# Task 3
a = int(input("Give a: "))
b = int(input("Give b: "))

if a >= b:
    print("Error, a must be less than b")
else:
    for n in range(a, b + 1):
        print(n, end=" ")   
    print()

# Task 4
n = int(input("Give a number: "))

for i in range(2, n + 1, 2):
    print(i, end=" ")
print()

# Task 5
total = 0.0
more = "y"

while more == "y":
    price = float(input("Item price: "))
    total += price
    more = input("Have more items? (y/n): ")

print(f"TOTAL: {round(total, 2)}")