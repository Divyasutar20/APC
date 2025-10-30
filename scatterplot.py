import matplotlib.pyplot as plt

x=[7,8,9,2,6,4,5,3]
y=[99,87.65,98,45,24,67,78,32,49,88]
plt.scatter(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Scatter Plot")
plt.savefig("scatterplot.png")
plt.show()
plt.close()
plt.legend(["Scatter 1"])