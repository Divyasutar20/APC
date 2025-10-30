import matplotlib.pyplot as plt

x=["A","B","C","D"]
y=[3,8,1,10]
plt.bar(x,y)
plt.xLabel("Categories")
plt.yLabel("Values")
plt.title("Simple Bar Plot")
plt.savefig("barplot.png")
plt.show()
plt.close()
plt.legend(["Bar 1"])
