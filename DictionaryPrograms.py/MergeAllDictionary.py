finalbag={}
size=int(input("Enter the size of dictionary:--"))
mybag1={}
for i in range(size):
    key=input('Enter the key ')
    value=input('Enter the value')
    mybag1.update({key:value})
print(mybag1)


size=int(input("Enter the size of second dictionary:--"))
mybag2={}
for i in range(size):
    key=input('Enter the key')
    value=input('Enter the value')
    mybag2.update({key:value})
print(mybag2)
for bigbag in(mybag1,mybag2):finalbag.update(bigbag)
print(finalbag)