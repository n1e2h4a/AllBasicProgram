table = []
number = int(input("Enter number of digit you want to print:---"))
for x in range(number):
    Element = int((input(' > ')))
    table.append(Element)
table.sort()
print("Smallest in List:", *table[:1])