number = int(input("Enter number of digit you want to print:---"))
newlist = []
for x in range(number):
    Element = int((input(' > ')))
    newlist.append(Element)
for y in newlist:
    print('%' * y)