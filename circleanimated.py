import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

circle = plt.Circle((1, 0), 0.2)
ax.add_patch(circle)

def update(frame):
    x = np.cos(frame)
    y = np.sin(frame)
    circle.center = (x, y)
    return circle,

ani = FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 2*np.pi, 100),
    interval=50
)

plt.show()
