size = int(input("Enter the size of dictionary:--"))
mybag = {}
for i in range(size):
    key = int(input('Enter the key '))
    value=key*key
    mybag.update({key: value})
print(mybag)