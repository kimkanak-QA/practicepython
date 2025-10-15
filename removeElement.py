'''
Q2:
Start with:

colors = ["red", "blue", "green"]


👉 Do the following step by step:

Add "yellow" at the end

Insert "black" at index 1

Remove "green"

Print the final list
'''

colors = ["red", "blue", "green"]
add = colors.append("yellow")
print("New list after adding yellow at end :",colors)

between = colors.insert(1,"black")
print("New list after inserting black at 1 :",colors)

rmv = colors.remove("green")
print("New list after removing green :",colors)