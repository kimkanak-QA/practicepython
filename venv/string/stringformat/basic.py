name = "Kanak"
age = 38


print("My name is {} and I am {} years old.".format(name, age))

''' positional index'''

(print("I am {1} years old and my name is {0}.".format(name, age)))

'''name placeholder'''

print("My name is {n} and my age is {a}.".format(n="Kanak", a=38))

'''f string'''

name = "Kanak"
age = 38
print(f"My name is {name} and I am {age} years old.")

pi = 3.14159265
print(f"Pi value is {pi:.2f}")

from datetime import datetime
today = datetime.now()
print(f"Today's date: {today:%d-%m-%Y}")