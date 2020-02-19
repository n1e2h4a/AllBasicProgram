group = [{"name": "neha"}, {"roll": "1"}, {"VI": "3"}, {"VI": "3"}, {"neha": "kl"}, {"hi": "45"}, {"rt": "kl"}]
print("Original List: ", group)
uniqvalue = set(val for dic in group for val in dic.values())
print("Unique Values: ", uniqvalue)