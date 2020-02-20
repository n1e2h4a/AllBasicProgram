def sumoflist(table):
    listmulti= 1
    for value in table:
        listmulti *= value
    return listmulti


table = []
number = int(input("Enter number of digit you want to print:---"))
for x in range(number):
    Element = int((input(' > ')))
    table.append(Element)
print(sumoflist(table))
