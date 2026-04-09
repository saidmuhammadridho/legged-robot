import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_robot():

    # Panjang masing-masing link
    link_lengths = [8, 6, 4]

    # Waktu simulasi
    time = np.linspace(0, 40, 1200)

    # Gerakan joint baru: kombinasi sin & cos agar lebih kompleks
    q1 = 0.7*np.sin(0.3*time) + 0.2*np.cos(0.6*time)
    q2 = 0.5*np.sin(0.8*time + np.pi/4) - 0.1*np.cos(1.5*time)
    q3 = 0.3*np.cos(1.0*time + np.pi/3) + 0.1*np.sin(2*time)

    # Setup figure
    fig, ax = plt.subplots(figsize=(7,7))
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_aspect('equal')
    ax.set_xlabel("X [units]")
    ax.set_ylabel("Y [units]")
    ax.set_title("3-Link Planar Robot - Forward Kinematics (New Motion)")
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.axhline(0, color='grey', lw=1)
    ax.axvline(0, color='grey', lw=1)

    # Workspace area
    R = sum(link_lengths)
    circle = plt.Circle((0,0), R, color='orange', alpha=0.1)
    ax.add_patch(circle)

    # Plot elements
    robot_line, = ax.plot([], [], 'b-', lw=3)
    robot_joints, = ax.plot([], [], 'ro', markersize=5)
    path_line, = ax.plot([], [], 'g--', lw=1)

    # Info box
    info_box = ax.text(
        0.02, 0.98, '', transform=ax.transAxes,
        fontsize=10, va='top', ha='left',
        bbox=dict(facecolor='white', alpha=0.8)
    )

    # Histori end-effector
    x_path, y_path = [], []

    def step(frame):
        # Ambil sudut saat ini
        th1, th2, th3 = q1[frame], q2[frame], q3[frame]

        # Forward kinematics
        x_positions = [0]
        y_positions = [0]

        # Hitung posisi tiap joint
        x_positions.append(x_positions[-1] + link_lengths[0]*np.cos(th1))
        y_positions.append(y_positions[-1] + link_lengths[0]*np.sin(th1))

        x_positions.append(x_positions[-1] + link_lengths[1]*np.cos(th1+th2))
        y_positions.append(y_positions[-1] + link_lengths[1]*np.sin(th1+th2))

        x_positions.append(x_positions[-1] + link_lengths[2]*np.cos(th1+th2+th3))
        y_positions.append(y_positions[-1] + link_lengths[2]*np.sin(th1+th2+th3))

        # Update robot
        robot_line.set_data(x_positions, y_positions)
        robot_joints.set_data(x_positions, y_positions)

        # Update trajectory
        x_path.append(x_positions[-1])
        y_path.append(y_positions[-1])
        path_line.set_data(x_path, y_path)

        # Update info
        info_text = (
            f"Joint angles:\nθ1={np.degrees(th1):.1f}°, θ2={np.degrees(th2):.1f}°, θ3={np.degrees(th3):.1f}°\n"
            f"End-effector:\nX={x_positions[-1]:.2f}, Y={y_positions[-1]:.2f}"
        )
        info_box.set_text(info_text)

        return robot_line, robot_joints, path_line, info_box

    # Animasi
    anim = FuncAnimation(fig, step, frames=len(time), interval=25)
    plt.show()

# Jalankan animasi
animate_robot()