import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Create figure and axis
fig, ax = plt.subplots()

# Initial circle
circle = Circle((0.5, 0.5), 0.1, color='blue')
ax.add_patch(circle)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# Key press function
def on_key(event):
    x, y = circle.center
    
    if event.key == 'up':
        y += 0.05
    elif event.key == 'down':
        y -= 0.05
    elif event.key == 'left':
        x -= 0.05
    elif event.key == 'right':
        x += 0.05
    
    circle.center = (x, y)
    fig.canvas.draw()

# Connect key press event
fig.canvas.mpl_connect('key_press_event', on_key)

plt.title("Use Arrow Keys to Move the Circle")
plt.show()