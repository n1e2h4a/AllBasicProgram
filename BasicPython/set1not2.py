a = {"White", "Black", "Red"}
b = {"Red", "Green"}
t = []
# storing a content in color
for color in a:
    # comparing between the sets
    if color not in b:
    # print the color
     print(f'the color which is not present in second set ', color)
