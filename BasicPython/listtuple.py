newlist = []
number = int(input("Enter number of digit you want to print:---"))
if number > 0:
    for x in range (number):
        Element = (input())
        newlist.append(Element)
        Tupleform = tuple(newlist)
print(f' list in tuple form {Tupleform}')
print(f' list in newlist form {newlist}')