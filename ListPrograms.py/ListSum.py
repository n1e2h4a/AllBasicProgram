def sumoflist(table):
    sumnum = 0
    for value in table:
        sumnum += value
    return sumnum


table = []
number = int(input("Enter number of digit you want to print:---"))
for x in range(number):
    Element = int((input(' > ')))
    table.append(Element)
print(sumoflist(table))
