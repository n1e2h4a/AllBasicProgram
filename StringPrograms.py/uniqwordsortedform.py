name=input('enter the comma seprated sequence of words')
words=[word for word in name.split((","))]
print(",".join(sorted(list(set(words)))))