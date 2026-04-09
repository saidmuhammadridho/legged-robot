import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def run_inverse():

    # Panjang link
    L1, L2, L3 = 8, 6, 4

    # Waktu
    t = np.linspace(0, 2*np.pi, 1000)

    # Target trajectory
    x_traj = 10*np.sin(2*t)
    y_traj = 8*np.cos(3*t)

    # Figure
    fig, ax = plt.subplots(figsize=(7,7))

    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_aspect('equal')

    # Axis & grid
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Inverse Kinematics - Trajectory Tracking")
    ax.grid(True, linestyle='--', alpha=0.5)

    # Garis sumbu
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)

    # Plot elemen
    line, = ax.plot([], [], lw=3, label="Robot")
    joints, = ax.plot([], [], 'o')

    target_plot, = ax.plot([], [], 'x', label="Target")
    traj, = ax.plot([], [], lw=1, label="End-Effector Path")

    ax.legend()

    # 🔥 Info kanan bawah
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

        x = x_traj[i]
        y = y_traj[i]

        phi = 0.5*np.sin(i*0.02)

        # ================= IK =================
        xw = x - L3*np.cos(phi)
        yw = y - L3*np.sin(phi)

        D = (xw**2 + yw**2 - L1**2 - L2**2)/(2*L1*L2)
        D = np.clip(D, -1, 1)

        theta2 = np.arccos(D)

        theta1 = np.arctan2(yw, xw) - np.arctan2(
            L2*np.sin(theta2),
            L1 + L2*np.cos(theta2)
        )

        theta3 = phi - theta1 - theta2

        # ================= FK (validasi) =================
        x1 = L1*np.cos(theta1)
        y1 = L1*np.sin(theta1)

        x2 = x1 + L2*np.cos(theta1+theta2)
        y2 = y1 + L2*np.sin(theta1+theta2)

        x3 = x2 + L3*np.cos(theta1+theta2+theta3)
        y3 = y2 + L3*np.sin(theta1+theta2+theta3)

        # ================= Plot =================
        line.set_data([0, x1, x2, x3], [0, y1, y2, y3])
        line.set_color("orange")

        joints.set_data([0, x1, x2, x3], [0, y1, y2, y3])
        joints.set_color("black")

        target_plot.set_data([x], [y])
        target_plot.set_color("red")

        # Trajectory aktual
        x_hist.append(x3)
        y_hist.append(y3)
        traj.set_data(x_hist, y_hist)
        traj.set_color("blue")

        # ================= ERROR =================
        error = np.sqrt((x - x3)**2 + (y - y3)**2)

        # ================= INFO TEXT =================
        info = (
            "=== JOINT ANGLE ===\n"
            f"θ1 = {np.degrees(theta1):6.2f}°\n"
            f"θ2 = {np.degrees(theta2):6.2f}°\n"
            f"θ3 = {np.degrees(theta3):6.2f}°\n\n"
            "=== TARGET ===\n"
            f"X = {x:6.2f}\n"
            f"Y = {y:6.2f}\n\n"
            "=== END-EFFECTOR ===\n"
            f"X = {x3:6.2f}\n"
            f"Y = {y3:6.2f}\n\n"
            f"Error = {error:6.4f}"
        )
        info_text.set_text(info)

        return line, joints, target_plot, traj, info_text

    # Animasi
    anim = FuncAnimation(fig, update, frames=len(t), interval=30)

    plt.show()


# Jalankan
run_inverse()