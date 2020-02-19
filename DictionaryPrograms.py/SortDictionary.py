import operator
Register={1:2, 3:4, 7:1, 8:0}
print("our unsorted dictionary :",Register)
sorted_Register=sorted(Register.items(),key=operator.itemgetter(1))
print("Dictionary in Asecending order by value:" ,sorted_Register)
sorted_Register=sorted(Register.items(),key=operator.itemgetter(1),reverse=True)
print("Dictionary in Descending order by value:" ,sorted_Register)
