Name = input("Enter any string:---")
Naming={}

for i in Name:
    Naming[i]= Naming.get(i, 0) + 1

print(Naming)