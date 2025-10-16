'''

Q1 — Even & Odd Separation

Given:

nums = [12, 7, 5, 64, 14, 23, 8]


Create two separate lists: one with even numbers, one with odd numbers.

Print both lists.
'''

nums = [12, 7, 5, 64, 14, 23, 8]
even = []
odd = []
for n in nums:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even :", even)
print("Odd :", odd)
