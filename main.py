from src.robot import update_pose
from src.controller import compute_wheel_speeds

import numpy as np
import matplotlib.pyplot as plt

x = 0
y = 0
theta = 0

vl = 20
vr = 20

wheel_base = 20
dt = 0.05

for frame in range(500):

    x, y, theta = update_pose(
        x, y, theta,
        vl, vr,
        wheel_base,
        dt
    )

    plt.cla()

    plt.xlim(-100,100)
    plt.ylim(-100,100)
    plt.axis("equal")
    plt.scatter(x, y, color="red")
    plt.arrow(
    x,
    y,
    np.cos(theta),
    np.sin(theta),
    head_width=3
    )
    plt.show()