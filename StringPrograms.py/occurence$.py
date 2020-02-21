def newchar(name):
    char= name[0]
    name=name.replace(char,'$')
    name=char + name[1:]
    return name
print(newchar('restart'))