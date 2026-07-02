import numpy as np

def update_pose(x, y, theta, vl, vr, wheel_base, dt):

    v = (vr + vl) / 2
    omega = (vr - vl) / wheel_base

    x += v * np.cos(theta) * dt
    y += v * np.sin(theta) * dt
    theta += omega * dt

    return x, y, theta