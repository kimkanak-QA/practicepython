""" Write a Python program that:

Takes a string input from the user.

Asks for a word to search.

Prints:

Whether the word exists

Its position if found

If the text starts or ends with that word
"""

text = input("Enter any statement: ")

if "money" in text:
    print("The word 'money' exists in the text.")
    print("Position of word 'money' is:", text.find("money"))

    if text.startswith("money"):
        print("‘money’ is at the start of the text.")
    elif text.endswith("money"):
        print("‘money’ is at the end of the text.")
    else:
        print("‘money’ is somewhere in the middle of the text.")
else:
    print("The word 'money' is not found in the text.")