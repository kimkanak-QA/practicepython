'''

Given:

nums = [45, 12, 89, 33, 22, 90, 10]


✅ Tasks:

Find the largest and smallest numbers using built-in functions (max() and min()).

Do the same using a loop — without using built-in functions.

'''

nums = [45, 12, 89, 33, 22, 90, 10]

print("Largest Number:", max(nums))
print("Smallest Number:", min(nums))

largest = nums[0]
smallest = nums[0]
for n in nums:
   if n > largest:
       largest = n
   if n < smallest:
       smallest = n

print("Largest Number:",largest)
print("Smallest Number:", smallest)
