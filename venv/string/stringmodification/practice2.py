"""

Write a Python program that:

Takes a comma-separated string of fruits (e.g. "apple,banana,cherry")

Splits it into a list and prints each fruit on a new line

"""
text = "apple,banana,cherry"
fruits = text.split(",")   # Split string using comma

print("List of fruits:", fruits)

print("\nPrinting each fruit one by one:")
for fruit in fruits:
    print(fruit)