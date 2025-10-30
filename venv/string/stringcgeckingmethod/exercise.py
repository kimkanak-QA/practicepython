""" Write a Python program that:

Takes user input

Prints whether the string is alphabetic, numeric, alphanumeric, or space-only

Also prints if it’s uppercase, lowercase, or title case"""

text = input("Enter any word: ")
if text.isalpha():
    print("string is alphabet")
elif text.isalnum():
    print("string is alphanumeric")
elif text.isnumeric():
    print("string is numeric")
elif text.isspace():
    print("string is space")
else:
    print("contains special character")

if text.isupper():
   print("string is uppercase")
elif text.islower():
   print("string is lowecase")
elif text.istitle():
   print("string is title")
else:
    print("mixed")
