import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_inverse_robot():

    # Panjang link
    links = [8, 6, 4]

    # Waktu
    time = np.linspace(0, 2*np.pi, 1000)

    # Trajectory target baru: kombinasi spiral + figure-eight
    x_target = 8*np.sin(2*time) + 5*np.cos(1.5*time)
    y_target = 6*np.cos(3*time) + 4*np.sin(2*time)

    # Setup figure
    fig, ax = plt.subplots(figsize=(7,7))
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_aspect('equal')
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("3-Link Planar Robot - Inverse Kinematics (New Trajectory)")
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.axhline(0, color='grey', lw=1)
    ax.axvline(0, color='grey', lw=1)

    # Robot plot
    robot_line, = ax.plot([], [], 'b-', lw=3)
    joints_plot, = ax.plot([], [], 'ko', markersize=5)
    target_point, = ax.plot([], [], 'rx', markersize=6)
    path_line, = ax.plot([], [], 'g--', lw=1)

    # Info box
    info_box = ax.text(
        0.02, 0.98, '', transform=ax.transAxes,
        fontsize=10, va='top', ha='left',
        bbox=dict(facecolor='white', alpha=0.8)
    )

    # Histori posisi end-effector
    x_path, y_path = [], []

    def step(frame):
        # Target saat ini
        xt, yt = x_target[frame], y_target[frame]

        # Orientasi end-effector lebih dinamis
        phi = 0.4*np.sin(frame*0.03 + np.pi/6) + 0.2*np.cos(0.05*frame)

        # ================= IK =================
        # Posisi wrist
        x_w = xt - links[2] * np.cos(phi)
        y_w = yt - links[2] * np.sin(phi)

        # Law of cosines
        cos_angle2 = (x_w**2 + y_w**2 - links[0]**2 - links[1]**2) / (2 * links[0] * links[1])
        cos_angle2 = np.clip(cos_angle2, -1, 1)
        theta2 = np.arccos(cos_angle2)

        theta1 = np.arctan2(y_w, x_w) - np.arctan2(links[1]*np.sin(theta2), links[0] + links[1]*np.cos(theta2))
        theta3 = phi - theta1 - theta2

        # ================= FK =================
        x1 = links[0] * np.cos(theta1)
        y1 = links[0] * np.sin(theta1)
        x2 = x1 + links[1] * np.cos(theta1 + theta2)
        y2 = y1 + links[1] * np.sin(theta1 + theta2)
        x3 = x2 + links[2] * np.cos(theta1 + theta2 + theta3)
        y3 = y2 + links[2] * np.sin(theta1 + theta2 + theta3)

        # ================= Plot =================
        robot_line.set_data([0, x1, x2, x3], [0, y1, y2, y3])
        joints_plot.set_data([0, x1, x2, x3], [0, y1, y2, y3])
        target_point.set_data([xt], [yt])

        x_path.append(x3)
        y_path.append(y3)
        path_line.set_data(x_path, y_path)

        # ================= Error =================
        err = np.sqrt((xt - x3)**2 + (yt - y3)**2)

        # ================= Info =================
        info_box.set_text(
            f"Joint angles:\nθ1={np.degrees(theta1):.1f}°, θ2={np.degrees(theta2):.1f}°, θ3={np.degrees(theta3):.1f}°\n"
            f"Target: X={xt:.2f}, Y={yt:.2f}\n"
            f"End-effector: X={x3:.2f}, Y={y3:.2f}\nError={err:.4f}"
        )

        return robot_line, joints_plot, target_point, path_line, info_box

    # Animasi
    anim = FuncAnimation(fig, step, frames=len(time), interval=30)
    plt.show()

# Jalankan
animate_inverse_robot()