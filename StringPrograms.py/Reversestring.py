def reversestring(name):
     name1=" "
     index =len(name)
     while index > 0:
         name1 += name[index -1 ]
         index = index -1
     return name1
print(reversestring("pythonnmae"))