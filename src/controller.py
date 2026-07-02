import numpy as np

def compute_wheel_speeds(x, y, theta, goal_x, goal_y, wheel_base):

    distance = np.sqrt((goal_x - x)**2 + (goal_y - y)**2)

    goal_theta = np.arctan2(goal_y - y, goal_x - x)

    heading_error = goal_theta - theta

    heading_error = np.arctan2(
        np.sin(heading_error),
        np.cos(heading_error)
    )

    K_linear = 0.8
    K_angular = 2.0

    linear = K_linear * distance
    angular = K_angular * heading_error

    max_speed = 25
    linear = np.clip(linear, -max_speed, max_speed)

    vl = linear - angular * wheel_base / 2
    vr = linear + angular * wheel_base / 2

    return vl, vr, distance