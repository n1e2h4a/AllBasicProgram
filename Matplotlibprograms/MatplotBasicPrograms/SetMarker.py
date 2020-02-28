import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,1,6,4]
plt.plot(x,y, color='red', linestyle='dashdot',linewidth = 2,marker ='o', markerfacecolor='blue', markersize=10)
plt.ylim(1,8)
plt.xlim(1,8)
plt.xlabel("I am x axis")
plt.ylabel("I am y axis")
plt.title("Display marker")
plt.show()