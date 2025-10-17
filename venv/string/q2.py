"""
Question 2: String Slicing Practice

Take a string from the user and print the following:

The first 3 characters

The last 3 characters

The middle part (excluding first and last 2 letters)

The reversed string
"""

text = input("Enter any string:")
print(text[0:3])
print(text[-3:])
print(text[2:-2])
print(text[::-1])