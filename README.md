🤖 3-Link Planar Robot Simulator
Simulasi interaktif robot planar 3-link berbasis Python yang menampilkan konsep Forward Kinematics (FK) dan Inverse Kinematics (IK) secara visual dan real-time.
Dirancang untuk membantu memahami pergerakan robot, hubungan antar joint, serta bagaimana robot mengikuti trajektori target.
________________________________________
✨ Preview Fitur
🔵 Forward Kinematics
•	Gerakan robot berdasarkan sudut joint 
•	Trajektori end-effector terlihat jelas 
•	Workspace robot divisualisasikan 
•	Informasi sudut dan posisi ditampilkan real-time 
🔴 Inverse Kinematics
•	Robot mengikuti lintasan target kompleks (spiral + figure-eight) 
•	Perhitungan sudut joint otomatis 
•	Error tracking antara target dan end-effector 
•	Visualisasi target & jalur pergerakan 
🎮 Interactive Menu
•	Pilih mode simulasi langsung dari terminal 
•	Mudah digunakan & modular 
________________________________________
🧠 Konsep yang Digunakan
•	Forward Kinematics (FK) 
•	Inverse Kinematics (IK) 
•	Trigonometri robotik 
•	Law of Cosines 
•	Animasi real-time dengan Matplotlib 
________________________________________
🛠️ Teknologi
•	Python 3.x 
•	NumPy 
•	Matplotlib 
________________________________________
📂 Struktur Project
3-link-robot-simulator/
│
├── forward_kinematics.py     # Simulasi FK (gerakan joint)
├── inverse_kinematics.py     # Simulasi IK (tracking target)
├── main.py                   # Menu interaktif
└── README.md
________________________________________
▶️ Cara Menjalankan
1.	Install dependency: 
pip install numpy matplotlib
2.	Jalankan program: 
python main.py
3.	Pilih mode: 
=== 3-Link Robot Simulator ===
1 - Forward Kinematics
2 - Inverse Kinematics
0 - Exit
________________________________________
⚙️ Cara Kerja
🔵 Forward Kinematics
•	Input: Sudut joint (θ1, θ2, θ3) 
•	Output: Posisi end-effector (X, Y) 
•	Menggunakan rumus trigonometri berantai 
🔴 Inverse Kinematics
•	Input: Target posisi (X, Y) 
•	Output: Sudut joint 
•	Menggunakan: 
o	Law of Cosines 
o	Pendekatan geometris 
________________________________________
🎯 Visualisasi yang Ditampilkan
•	Struktur robot (link & joint) 
•	Jalur end-effector 
•	Target trajectory (IK) 
•	Workspace robot 
•	Informasi numerik real-time: 
o	Sudut joint 
o	Posisi end-effector 
o	Error (IK) 
________________________________________
🔧 Kustomisasi
Kamu bisa dengan mudah mengubah:
Panjang Link
link_lengths = [8, 6, 4]
Pola Gerakan (FK)
q1 = 0.7*np.sin(0.3*time) + 0.2*np.cos(0.6*time)
Trajektori Target (IK)
x_target = 8*np.sin(2*time) + 5*np.cos(1.5*time)
________________________________________
💡 Use Case
•	Pembelajaran robotika dasar 
•	Visualisasi kinematics 
•	Eksperimen trajectory planning 
•	Demo presentasi teknik 
________________________________________
📌 Catatan Penting
•	Simulasi hanya bekerja pada bidang 2D (planar) 
•	Tidak mempertimbangkan dinamika (gaya, massa, dll) 
•	Fokus pada aspek kinematics

