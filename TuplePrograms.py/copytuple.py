import copy
 #shallow copy

old_list = ([1, 1, 1], [2, 2, 2], [3, 3, 3])
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Shallow Old list:", old_list)
print("Shallow New list:", new_list)




#Deep cloning

old_list = ([1, 1, 1], [2, 2, 2], [3, 3, 3])
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print(" Deep clone Old list:", old_list)
print("Deep clone New list:", new_list)