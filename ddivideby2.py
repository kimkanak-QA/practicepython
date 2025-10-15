'''

Given:

nums = [2, 4, 6, 8, 10]


✅ Tasks:

Create a new list where each number is divided by 2 — using a for loop.

Do the same using list comprehension.

'''

nums = [2, 4, 6, 8, 10]

list1 = []
for n in nums:
    list1.append(n/2)
print("by loop",list1)

half = [n/2 for n in nums]
print("by list comprehension",half)



