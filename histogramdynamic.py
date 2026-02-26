import matplotlib.pyplot as plt


user_input = input("Enter numbers separated by commas: ")


data = [float(x.strip()) for x in user_input.split(",")]


plt.hist(data, bins=5, edgecolor='black')
plt.title("Histogram from User Input")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
