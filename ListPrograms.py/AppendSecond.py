table1 = []
number = int(input("Enter number of digit you want to print in 1st list:---"))
for x in range(number):
    Element = int((input(' > ')))
    table1.append(Element)
print("my table1",table1)


table2 = []
number = int(input("Enter number of digit you want to print in 2nd list:---"))
for x in range(number):
    Element = int((input(' > ')))
    table2.append(Element)
print("my table2",table2)
Finallist=table1+table2
print(Finallist)