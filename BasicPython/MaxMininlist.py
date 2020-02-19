# enter the number for number of element you want to take in list
Number = int(input("Enter number of digit you want to print:---"))
minmax=[]
newlist1=[]
newlist2=[]
for x in range(Number):
    # input in list
    Element = int((input(' > ')))
    # empty list appended by the input
    minmax.append(Element)
print(minmax)

for list1 in minmax:
 current = minmax[0]
 if current > list1:
    current=list1
newlist1.append(current)
print("Minimum number is:--",newlist1)


for list1 in minmax:
 current = minmax[0]
 if current < list1:
    current=list1
newlist2.append(current)
print("Maximum number is:--",newlist2)

