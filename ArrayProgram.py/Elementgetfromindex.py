number = int(input("Enter number of digit you want to print:---"))
newlist = []
for x in range(number):
    # input in list
    Element = int((input(' > ')))
    # empty list appended by the input
    newlist.append(Element)
print(newlist)
indexwant = int(input("Enter the index number:---"))
for y in newlist:
    if indexwant == y:
        print(newlist[y])
