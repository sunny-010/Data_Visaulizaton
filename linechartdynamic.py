import matplotlib.pyplot as plt


x = list(map(float, input("Enter X values (comma separated): ").split(",")))
y = list(map(float, input("Enter Y values (comma separated): ").split(",")))


plt.plot(x, y, marker='o')
plt.title("User Input Line Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()
