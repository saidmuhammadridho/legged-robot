import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def run_forward():

    # Panjang link
    L1, L2, L3 = 8, 6, 4

    # Waktu
    t = np.linspace(0, 40, 1200)

    # Joint trajectory
    theta1 = 0.8*np.sin(0.5*t)
    theta2 = 0.6*np.sin(1.2*t + np.pi/3)
    theta3 = 0.4*np.cos(1.8*t + np.pi/6)

    # Figure
    fig, ax = plt.subplots(figsize=(7,7))

    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_aspect('equal')

    # Axis & grid
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Forward Kinematics - Joint Space Exploration")
    ax.grid(True, linestyle='--', alpha=0.5)

    # Garis sumbu
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)

    # Workspace
    r = L1 + L2 + L3
    theta = np.linspace(0, 2*np.pi, 200)
    ax.fill(r*np.cos(theta), r*np.sin(theta), alpha=0.1)

    # Robot
    line, = ax.plot([], [], lw=3)
    joints, = ax.plot([], [], 'o')

    # Trajectory
    traj, = ax.plot([], [], lw=1)

    # 🔥 Info di pojok kanan bawah (RELATIVE POSITION)
    info_text = ax.text(
        0.98, 0.02, '',
        transform=ax.transAxes,
        fontsize=10,
        color='black',
        ha='right',
        va='bottom',
        bbox=dict(facecolor='white', alpha=0.7)
    )

    x_hist, y_hist = [], []

    def update(i):
        t1 = theta1[i]
        t2 = theta2[i]
        t3 = theta3[i]

        # Forward Kinematics
        x1 = L1*np.cos(t1)
        y1 = L1*np.sin(t1)

        x2 = x1 + L2*np.cos(t1+t2)
        y2 = y1 + L2*np.sin(t1+t2)

        x3 = x2 + L3*np.cos(t1+t2+t3)
        y3 = y2 + L3*np.sin(t1+t2+t3)

        # Update robot
        line.set_data([0, x1, x2, x3], [0, y1, y2, y3])
        joints.set_data([0, x1, x2, x3], [0, y1, y2, y3])

        # Trajectory
        x_hist.append(x3)
        y_hist.append(y3)
        traj.set_data(x_hist, y_hist)

        # Info text
        info = (
            "=== JOINT ANGLE ===\n"
            f"θ1 = {np.degrees(t1):6.2f}°\n"
            f"θ2 = {np.degrees(t2):6.2f}°\n"
            f"θ3 = {np.degrees(t3):6.2f}°\n\n"
            "=== END-EFFECTOR ===\n"
            f"X = {x3:6.2f}\n"
            f"Y = {y3:6.2f}"
        )
        info_text.set_text(info)

        return line, joints, traj, info_text

    # Animasi
    anim = FuncAnimation(fig, update, frames=len(t), interval=25)

    plt.show()


# Jalankan
run_forward()