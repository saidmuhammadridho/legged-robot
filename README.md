🤖 3-DOF Planar Robot Simulation

Forward & Inverse Kinematics Visualization using Python

📖 Overview

This project presents a simulation of a 3 Degrees-of-Freedom (3-DOF) planar robotic arm.
It is designed to demonstrate the relationship between joint space (angles) and Cartesian space (end-effector position).

The simulation runs in real-time, allowing users to observe how the robot moves and how target positions are achieved through kinematic analysis.

🚀 Key Features
Real-time animation of a 3-link planar robot
Forward Kinematics (joint angles → position)
Inverse Kinematics using geometric approach
End-effector trajectory visualization
Target tracking capability
Error calculation between target and actual position
📁 Project Structure
Assignment 2/
│
├── main.py              # Main program (menu system)
├── forwardk.py         # Forward Kinematics simulation
├── inversek.py         # Inverse Kinematics simulation
└── README.md
▶️ How to Run
1. Install dependencies
pip install numpy matplotlib
2. Run the program
python main.py
3. Select simulation mode
1 → Forward Kinematics
2 → Inverse Kinematics
⚙️ Robot Configuration

The robot operates in a 2D plane and consists of three rigid links:

Link	Length
L1	8
L2	6
L3	4
📐 Forward Kinematics

Forward Kinematics computes the position of the end-effector based on given joint angles.

Each link contributes sequentially to the final position, forming a kinematic chain from the base to the end-effector.

📐 Inverse Kinematics (Geometric Approach)

Inverse Kinematics determines the joint angles required to reach a specific target position.

This implementation uses a geometric approach, which relies on triangle relationships between the robot links.

Process:
Compute wrist position (removing the last link contribution)
Form a triangle using link lengths
Calculate joint angles using trigonometry
Adjust the final joint to match orientation

This method is efficient, intuitive, and well-suited for planar robotic systems.

📊 Error Calculation

To measure tracking performance, position error is defined as:

Error = √((x_target − x_actual)² + (y_target − y_actual)²)

This value indicates how closely the end-effector follows the desired trajectory.

🧠 Insights

From this simulation, we can observe:

The relationship between joint motion and end-effector position
The reverse mapping solved by inverse kinematics
The effectiveness of geometric methods for planar robots
Real-time trajectory tracking behavior
📌 Notes
This project is intended for educational purposes
Suitable for learning basic robotics concepts
Can be extended to more advanced robotic systems
📄 License

This project is developed for academic and learning purposes.
