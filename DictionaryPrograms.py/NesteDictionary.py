num_list = [10, 100, 1000, 10000]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)