table = []
uniq=[]

number = int(input("Enter number of digit you want to print:---"))
for x in range(number):
    Element = int((input(' > ')))
    table.append(Element)
for x in table:
     if x not in uniq:
        uniq.append(x)

print("the uniq list without dublicate element:--",uniq)