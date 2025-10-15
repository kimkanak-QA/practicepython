'''

Given:

items = ["apple", "banana", "apple", "cherry", "banana", "apple"]


✅ Tasks:

Find how many times "apple" appears in the list.

Remove all "banana" items from the list.

Print the final list after removing "banana".
'''

items = ["apple", "banana", "apple", "cherry", "banana", "apple"]

print("number of apple: " , items.count("apple"))

while "banana" in items:

  items.remove("banana")

print(items)