"""

isalpha()   alphabet
isalnum()   alphanumeric
isdigit()   digit
isupper() / islower() / istitle()
isspace()  space
"""

text = "hello"
print(text.isalpha())
text = "hello123"
print(text.isalpha())

text = "hello"
print(text.isalnum())
text = "hello123!"
print(text.isalnum())

text = "1234"
print(text.isdigit())
text = "hello123!"
print(text.isdigit())

text = " "
print(text.isspace())
text = ""
print(text.isspace())

text = "hello"
print(text.isupper())
text = "HELLO"
print(text.isupper())

text = "hello"
print(text.islower())
text = "HELLO"
print(text.islower())

text = "Hello"
print(text.istitle())
text = "eHllow"
print(text.istitle())