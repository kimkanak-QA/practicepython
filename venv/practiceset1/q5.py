'''

Given the list:

nums = [12, 45, 2, 67, 23, 89, 10]


✅ Task:

Find the second largest number in the list.

Find the second smallest number in the list.

'''

nums = [12, 45, 2, 67, 23, 89, 10]
nums.sort()
print(nums)
second_largest = nums[-2]
second_smallest = nums[1]

print("the second largest number in the list is: ", second_largest)
print("the second smallest number in the list is: ", second_smallest)