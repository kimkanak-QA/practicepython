"""
Write a Python program that:

Takes a string as input

Counts how many vowels and consonants are in it

Ignores spaces, numbers, and special characters

"""
text = input("Enter any string: ").lower()  # convert to lowercase
vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():               # check only letters
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)