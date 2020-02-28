import matplotlib.pyplot as plt
x1=[10,20,30]
y1=[20,40,10]
plt.plot(x1,y1, label = "this is line first" )
x2=[10,20,30]
y2=[40,10,30]
plt.plot(x2,y2, label = "this is line second")
plt.xlabel("I am x axis")
plt.ylabel("I am y axis")
plt.title("Two or more lines on same plot with good legend")
plt.plot(x1,y1, color ='green' , linewidth = 3, label = 'line1-width-3')
plt.plot(x2,y2, color ='black' , linewidth = 5, label = 'line1-width-5')
plt.legend()
plt.show()