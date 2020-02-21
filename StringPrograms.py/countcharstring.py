def frequency (site):
    new = {}
    for n in site:
        keys = new.keys()
        if n in keys:
            new[n] += 1
        else:
            new[n] = 1
    return new
print(frequency("google.com"))