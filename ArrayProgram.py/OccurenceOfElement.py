number = int(input("Enter number of digit you want to print in list:---"))
occur= int(input("Enter number to find the occurence:---"))
newlist=[]
count=0

def countx(newlist,xy):
    return newlist.count(xy)

for x in range(number):
 Element = int((input(' > ')))
 newlist.append(Element)
print(newlist)

print(' {} has occured {} times'.format(occur, countx(newlist, occur)))
