size = int(input("Enter the size of dictionary:--"))
mybag = {}
for i in range(size):
    key = input('Enter the key ')
    value = input('Enter the value')
    mybag.update({key: value})
print(mybag)
key2 = input("Enter the key which you want to remove:--")
if key2 in mybag:
    del mybag[key2]
else:
    print("key not found!")
    exit(0)
print("Final dictionary")
print(mybag)
