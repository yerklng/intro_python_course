# Task 1
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(celsius_to_fahrenheit(100))   # 212.0
print(fahrenheit_to_celsius(212))   # 100.0
print(factorial(5))                 # 120
print(factorial(0))                 # 1


# Task 2
import random

# First list: 20 random integers from 1 to 100
list1 = []
for s in range(20):
    list1.append(random.randint(1, 100))
print("List 1:", list1)

# Even numbers and their total
evens = []
total = 0
for n in list1:
    if n % 2 == 0:
        evens.append(n)
        total += n
print("Even numbers:", evens)
print("TOTAL of even numbers:", total)

# Second list and common elements
list2 = []
for s in range(20):
    list2.append(random.randint(1, 100))
print("List 2:", list2)

common = []
for n in list2:
    if n in list1 and n not in common:
        common.append(n)
print("In both lists:", common)


# Task 3
data = [
    [2020, 2.3, 2.2, 1.8, 3.1],
    [2021, 2.4, 2.0, 1.7, 3.0],
    [2022, 1.7, 1.2, 1.0, 1.8],
    [2023, 1.9, 1.0, 0.7, 2.0],
    [2024, 2.0, 2.4, 2.0, 3.2],
]

# a. Total sales per year
print("Total sales per year:")
for row in data:
    year = row[0]
    total = sum(row[1:])
    print(f"{year}: {round(total, 2)}")

# b. Average sales per quarter, per year
print("\nAverage sales per quarter, per year:")
for row in data:
    year = row[0]
    avg = sum(row[1:]) / 4
    print(f"{year}: {round(avg, 2)}")

# c. Max and min sales (year and quarter)
max_sales = data[0][1]
min_sales = data[0][1]
max_year, max_q = data[0][0], 1
min_year, min_q = data[0][0], 1

for row in data:
    for q in range(1, 5):
        value = row[q]
        if value > max_sales:
            max_sales = value
            max_year, max_q = row[0], q
        if value < min_sales:
            min_sales = value
            min_year, min_q = row[0], q

print(f"\nMax sales: {max_sales} in {max_year}, quarter {max_q}")
print(f"Min sales: {min_sales} in {min_year}, quarter {min_q}")