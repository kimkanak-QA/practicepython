'''

Count how many times the letter 'a' appears in this string:
"automation and api testing"

'''

text = "automation and api testing"
count = 0
for ch in text:
    if ch == "a":
        count += 1
print( count, "no of a appears in the text " )

''' also use count function '''
print(text.count("a"))