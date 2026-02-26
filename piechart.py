import matplotlib.pyplot as plt


sizes = [30, 20, 25, 25]  
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']  


plt.pie(sizes, labels=labels)

plt.title("Basic Pie Chart")
plt.show()
