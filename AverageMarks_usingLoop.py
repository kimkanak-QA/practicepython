'''
Given:

marks = [55, 67, 80, 45, 90]


✅ Tasks:

Find the average marks using a loop

Find the average marks using built-in functions (sum() and len())

'''
marks = [55, 67, 80, 45, 90]
total = 0
for i in marks:
    total += i

avg = total/(len(marks))
print("average using loop is: ",(avg))

average = sum(marks)/len(marks)

print("average using built in sum & length is: ",(average))

