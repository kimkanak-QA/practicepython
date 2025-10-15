'''
Count & Search
Q4:

items = ["pen", "pencil", "eraser", "pen", "scale", "pen"]


👉 Find:

How many times "pen" occurs

The index of the first "eraser"
'''

items = ["pen", "pencil", "eraser", "pen", "scale", "pen"]

count = 0

for c in items:
 if c== "pen":
    count += 1

print("pen has occured :", count, "times")


for i in items:
 if i == "eraser":
    print(items.index(i))

