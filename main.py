from src.robot import update_pose
from src.controller import compute_wheel_speeds

import numpy as np
import matplotlib.pyplot as plt


wheel_base = 20
dt = 0.05

x = -60
y = -60
theta = np.radians(0)

goal_x = 60
goal_y = 40

trail = []

plt.figure(figsize=(8,8))

for frame in range(1000):

    vl, vr, distance = compute_wheel_speeds(
        x,
        y,
        theta,
        goal_x,
        goal_y,
        wheel_base
    )

    x, y, theta = update_pose(
        x,
        y,
        theta,
        vl,
        vr,
        wheel_base,
        dt
    )

    trail.append((x,y))

    plt.cla()

    plt.axis("equal")
    plt.xlim(-100,100)
    plt.ylim(-100,100)

    plt.grid(True)

    plt.title("Differential Drive Robot")

    plt.scatter(goal_x, goal_y, color="green", marker="x", s=100)

    plt.plot([p[0] for p in trail], [p[1] for p in trail], color="orange")

    plt.scatter(x, y, color="red", s=100)

    plt.arrow(x, y, 10*np.cos(theta), 10*np.sin(theta), head_width=3, head_length=4, color="blue")

    plt.pause(0.01)

    if distance < 2:
        print("Goal Reached!")
        break

plt.show()