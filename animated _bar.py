import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


categories = ['A', 'B', 'C', 'D', 'E']
num_bars = len(categories)

np.random.seed(42)
values = np.random.randint(1, 10, size=num_bars)

fig, ax = plt.subplots()
bars = ax.bar(categories, values, color='red')


ax.set_ylim(0, 15)
ax.set_title("Dynamic Bar Chart", fontsize=16)
ax.set_ylabel("Value")


def update(frame):
    new_values = np.random.randint(1, 15, size=num_bars)
    for bar, new_val in zip(bars, new_values):
        bar.set_height(new_val)
    return bars


ani = FuncAnimation(fig, update, frames=50, interval=500, blit=False, repeat=True)


plt.tight_layout()
plt.show()
