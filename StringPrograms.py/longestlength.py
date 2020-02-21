def longstring(listofwords):
    stringholder=[]
    for n in listofwords:
        stringholder.append((len(n),n))
    stringholder.sort()
    return stringholder[-1][1]
print(longstring(["blackberry","nokia","Reliance","oppo"]))

