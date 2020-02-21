def addstring(name):
    length =len(name)
    if length > 2:
        if name[-3:]== 'ing':
            name += 'ly'
        else:
            name += 'ing'
    return name
print(addstring("As"))
print(addstring("simple"))
print(addstring("sleeping"))