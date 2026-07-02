# Differential Drive Robot Navigation

A Python simulation of a differential drive mobile robot capable of autonomously navigating to any target point using differential drive kinematics and proportional control.

---

## Features

- Differential drive robot simulation
- Forward kinematics of mobile robot
- Proportional (P) controller
- Real-time trajectory visualization
- Interactive goal selection using mouse clicks
- Smooth robot animation using Matplotlib

---

## Project Structure

```
.
├── main.py
├── src
|    ├── robot.py
|    └── controller.py
└── README.md
```

---

## Working Principle

The robot continuously computes the distance and heading error to the target point.

A proportional controller generates the required linear and angular velocities, which are converted into left and right wheel speeds.

The robot pose is then updated using differential drive kinematics and the process repeats until the goal is reached.

---

## Differential Drive Kinematics

Linear velocity

$v=\frac{V_R+V_L}{2}$

Angular velocity

$\omega=\frac{V_R-V_L}{L}$

Robot motion

$\dot{x}=v\cos\theta$

$\dot{y}=v\sin\theta$

$\dot{\theta}=\omega$

---

## Controller

Distance to goal

$d=\sqrt{(x_g-x)^2+(y_g-y)^2}$

Heading to goal

$\theta_g=\operatorname{atan2}(y_g-y,\;x_g-x)$

The proportional controller computes

- Linear velocity
- Angular velocity

which are converted into left and right wheel speeds.

---

## Requirements

Install the required libraries:

```bash
pip install numpy matplotlib
```

---

## Running the Project

```bash
python main.py
```

---

## Interactive Simulation

Click anywhere inside the simulation window to assign a new goal.

The robot automatically rotates toward the selected point and navigates to it while continuously updating its orientation.

---

## Concepts Used

- Differential Drive Kinematics
- Mobile Robot Modeling
- Proportional Control
- Trajectory Generation
- Euler Integration
- Robot Simulation
- Interactive Motion Planning

---

## Video Demonstration

<video src='diff_drive_recording.webm' width='100%' controls></video>

---

## Challenges

- Computing robot orientation correctly.
- Converting controller outputs into wheel velocities.
- Normalizing heading error.
- Tuning controller gains for smooth motion.
- Interactive target selection using mouse events.

---

## Future Improvements

- PID controller
- Obstacle avoidance
- Waypoint navigation
- Pure Pursuit controller
- Stanley controller
- A* and RRT path planning
- ROS2 implementation
- Pygame visualization

---

## Demo

The simulation demonstrates a differential drive robot autonomously navigating toward user-selected target points using feedback control and differential drive kinematics.