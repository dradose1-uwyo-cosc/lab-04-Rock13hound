items = ["milk","Bananas","eggs","Granola","Avocado"]
prices = [2, 1, 3.5, 2.5, .58]

for index in range(len(items)):
    print(f"I bought {items[index]} for ${prices[index]}")

total = 0
for price in prices:
    total = price + total
print(f"I paid ${total} for everything")

#max(prices)
#print({index}