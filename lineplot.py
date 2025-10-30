import matplotlib .pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.xlim(0,6)
plt.ylim(0,12)
plt.grid()
plt.title("simple Line Plot")
plt.plot(x,y)
plt.show()
plt.savefig("lineplot.png")
plt.legend(["Line 1"])
plt.close()
