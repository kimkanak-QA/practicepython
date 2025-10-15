'''

Create a list of numbers from 1 to 10.

Print only the first 3 numbers.

Print the last 3 numbers using negative indexing.

Print every second number (skip one each time).

'''

number = [1,2,3,4,5,6,7,8,9,10]
print("First 3 number:", number[:3])
print("last 3 number:", number[-3:])
print("Every second number:", number[::2])