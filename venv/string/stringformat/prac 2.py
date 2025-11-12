"""

Take

price = 49.5678


and display:

Price after formatting: 49.57


using both
👉 .format() and
👉 f-string (show only 2 decimal places).
"""

price = 49.5678
print("Price after formatting: {:.2f}".format(price))
print(f"Price after formatting: {price:.2f}")
