import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 10, 5]

plt.plot(x, y)
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Simple Plot')
plt.grid(True)
# plt.show()
plt.savefig('plot.png')
