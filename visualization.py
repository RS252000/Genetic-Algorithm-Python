import matplotlib.pyplot as plt


x = [point[0] for point in data]
y = [point[1] for point in data]


plt.scatter(x, y, marker='s',color='forestgreen', s=200)
for i, point in enumerate(data):
    plt.text(point[0], point[1], str(i+1), ha='center', va='center', color='white', fontsize=11)


plt.xlim(100, 500)
plt.ylim(13, 30)


plt.xlabel('Sum of nutrients')
plt.ylabel('Price')
plt.title('Representation of the best individuals')


plt.show()
