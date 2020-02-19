size = int(input("Enter the size of dictionary:--"))
mybag = {}
for i in range(size):
    key = input('Enter the key ')
    value = input('Enter the value')
    mybag.update({key: value})
print(mybag)
for bigkey, value in mybag.items():
    print(bigkey, "indicate", mybag[bigkey])
