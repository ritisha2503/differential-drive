from src.robot import update_pose
from src.controller import compute_wheel_speeds

import numpy as np
import matplotlib.pyplot as plt


wheel_base = 20
dt = 0.05

x = -60
y = -60
theta = np.radians(0)

goal_x = x
goal_y = y

trail = []

fig, ax = plt.subplots(figsize=(8, 8))

def onclick(event):
    global goal_x, goal_y

    if event.xdata is None or event.ydata is None:
        return

    goal_x = event.xdata
    goal_y = event.ydata

    print(f"New Goal: ({goal_x:.2f}, {goal_y:.2f})")

fig.canvas.mpl_connect('button_press_event', onclick)

while True:

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

    ax.clear()

    ax.set_aspect('equal')
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)

    ax.grid(True)

    ax.set_title("Click anywhere to move the robot")

    ax.scatter(goal_x, goal_y, color="green", marker="x", s=100)

    ax.plot([p[0] for p in trail], [p[1] for p in trail], color="orange")

    ax.scatter(x, y, color="red", s=100)

    ax.arrow(x, y, 10*np.cos(theta), 10*np.sin(theta), head_width=3, head_length=4, color="blue")

    plt.pause(0.01)