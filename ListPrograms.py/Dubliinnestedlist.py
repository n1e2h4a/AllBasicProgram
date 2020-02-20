import itertools
rank = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original List", rank)
rank.sort()
new_num = list(num for num,variable in itertools.groupby(rank))
print("New List", new_num)
