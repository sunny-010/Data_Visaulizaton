import pandas as pd
import numpy as np
import plotly.express as px


np.random.seed(42)
n_points = 20
n_frames = 30


data = []
for t in range(n_frames):
    x = np.random.rand(n_points) * 10
    y = np.random.rand(n_points) * 10
    size = np.random.randint(10, 50, n_points)
    group = np.random.choice(['A', 'B'], n_points)
    for i in range(n_points):
        data.append([t, x[i], y[i], size[i], group[i]])

df = pd.DataFrame(data, columns=['time', 'x', 'y', 'size', 'group'])


fig = px.scatter(
    df,
    x="x",
    y="y",
    animation_frame="time",
    animation_group="group",
    size="size",
    color="group",
    range_x=[0, 10],
    range_y=[0, 10],
    title="Dynamic Scatter Plot (Animated)",
    labels={"x": "X Axis", "y": "Y Axis"}
)


fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 200


fig.show()
