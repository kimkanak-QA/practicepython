'''

Q6:
👉 Create a list of squares of numbers from 1 to 10 using a single line of code (list comprehension).

Expected Output:

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''

square = squares = [x*x for x in range(1, 11)]
print(square)