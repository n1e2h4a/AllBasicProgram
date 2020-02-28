import matplotlib.pyplot as plt
x =range(1,50)
y =[value * 3 for value in x]
print("values of x:")
print(*range(1,50))
print("values of y (thrice of x):")
print(y)
plt.plot(x,y)
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Draw line")
plt.show()


x= list(range(1,11))
y= list(range(10,101,10))

plt.plot(x,y)
plt.show()