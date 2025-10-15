
text = input("Enter string: ")
ch = input("Enter character to count: ")

count = 0
for c in text:
    if c == ch:
        count += 1

print("No of", ch, "in", text, "is:", count)