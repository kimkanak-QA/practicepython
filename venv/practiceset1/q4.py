'''
Given a list of marks:

marks = [45, 67, 88, 23, 90, 49, 55]


✅ Task:
Count how many numbers in the list are greater than 50.
'''

marks = [45, 67, 88, 23, 90, 49, 55]
count = 0
for n in marks:
    if n > 50 :
     count += 1
print("the number of list greater than 50 are :", count)

'''
count = 0 → start counting from 0

for n in marks: → loop through each number

if n > 50: → check if number is greater than 50

count += 1 → increase count if condition is true
'''