import numpy as np

def update_pose(x, y, theta,
                vl, vr,
                wheel_base,
                dt):
    v = (vl + vr)/2
    omega = (vr - vl)/wheel_base
    x += v * dt * np.cos(theta)
    y += v * dt * np.sin(theta)
    theta += omega * dt
    return x, y, theta