'''
✅ Q1:

Write a program to reverse a string.
Input: "python"
Output: "nohtyp"
'''

text = input("Enter any string: ")
rev =""
for ch in text:
    rev = ch + rev
print(rev)