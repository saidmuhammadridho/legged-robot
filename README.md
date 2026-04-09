🤖 3-DOF Planar Robot Simulation

Interactive Visualization of Forward and Inverse Kinematics using Python

📖 Overview

This project demonstrates a simulation of a 3 Degrees-of-Freedom (3-DOF) planar robotic arm. The purpose of this simulation is to study the relationship between joint space (angles) and Cartesian space (end-effector position).

The system provides real-time visualization, allowing users to observe how joint movements affect the robot and how a target position can be reached using inverse kinematics.

🚀 Key Features
Real-time animation of a 3-link planar robot
Forward Kinematics (joint angles → position)
Inverse Kinematics using geometric approach (position → joint angles)
End-effector trajectory visualization
Target tracking system
Error calculation between desired and actual position
📁 Project Structure

.
├── main.py # Main program (menu system)
├── forwardk.py # Forward Kinematics simulation
├── inversek.py # Inverse Kinematics simulation
└── README.md

▶️ How to Run
Install required libraries
pip install numpy matplotlib
Run the program
python main.py
Select simulation mode
1 → Forward Kinematics
2 → Inverse Kinematics
⚙️ Robot Configuration

The robot consists of three rigid links operating in a 2D plane:

Link 1 (L1) = 8
Link 2 (L2) = 6
Link 3 (L3) = 4

📐 Forward Kinematics

Forward Kinematics is used to compute the position of the end-effector based on given joint angles.

The calculation is performed sequentially from the base to the end-effector, where each link contributes to the final position. This creates a chain of transformations that determines the robot's final pose.

📐 Inverse Kinematics (Geometric Approach)

Inverse Kinematics is used to determine the joint angles required to reach a specific target position.

This project uses a geometric method, which is based on triangle relationships between robot links. The process includes:

Determining the wrist position by removing the last link contribution
Forming a triangle using link lengths
Computing angles using trigonometric relationships
Adjusting the final joint to match orientation

This approach is efficient and intuitive for planar robotic systems.

📊 Error Calculation

To evaluate tracking performance, position error is calculated using:

Error = √((x_target − x_actual)² + (y_target − y_actual)²)

This value shows how accurately the robot follows the desired trajectory.

🧠 Insights

From this simulation, we can understand:

The mapping from joint space to task space (Forward Kinematics)
The reverse mapping from task space to joint space (Inverse Kinematics)
The effectiveness of geometric methods in solving planar IK problems
How trajectory tracking behaves in real-time systems
📌 Notes
This project is intended for educational purposes
Useful for learning basic robotic kinematics
Can be extended to more complex robotic systems
📄 License

This project is developed for academic and learning purposes.
