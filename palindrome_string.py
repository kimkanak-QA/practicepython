str= input("Enter any string : ")

reverse = ""
for ch in str:
    reverse = ch + reverse

if str == reverse:
    print(str, "is Palindrome")
else:
    print(str,"is not palindrome")