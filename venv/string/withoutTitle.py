'''
Convert the string "welcome to python world" → "Welcome To Python World" (each word capitalized

'''

text = "welcome to python world"
word = text.split()
cap =[]

for w in word:
    cap.append(w[0].upper() + w[1:])
    result = " ".join(cap)
print(result)