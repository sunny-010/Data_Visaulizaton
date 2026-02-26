import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y1 = [2, 4, 1, 8, 7]
y2 = [5, 3, 6, 2, 4]


fig, axes = plt.subplots(1, 2, figsize=(10, 4)) 


axes[0].plot(x, y1, color='blue', marker='o')
axes[0].set_title("Plot 1")


axes[1].plot(x, y2, color='red', marker='x')
axes[1].set_title("Plot 2")


plt.suptitle("Example of Subplots")

plt.show()
