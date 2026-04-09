🤖 Simulasi Robot Planar 3-Link (3-DOF)

Eksperimen Interaktif Forward & Inverse Kinematics dengan Python

🌟 Tentang Proyek

Bayangkan sebuah robot 3-link yang bergerak di bidang 2D.
Di proyek ini, kita bisa melihat sendi robot bergerak, end-effector mengikuti lintasan, dan target dicapai secara real-time.

Proyek ini membantu kamu memahami:

Bagaimana sudut tiap sendi memengaruhi posisi akhir robot
Bagaimana robot bisa menghitung sendiri sudut yang diperlukan untuk mencapai titik tertentu

Semua simulasi ditampilkan dalam animasi yang interaktif, sehingga belajar robotika jadi lebih seru! 🎉

🚀 Fitur Utama
🎥 Animasi interaktif robot 3-link
🔹 Forward Kinematics: hitung posisi end-effector dari sudut joint
🔹 Inverse Kinematics: hitung sudut joint dari target posisi (menggunakan metode geometri)
📈 Visualisasi lintasan end-effector secara real-time
🎯 Target tracking: lihat seberapa akurat robot mengikuti target
⚡ Evaluasi error posisi otomatis
📂 Struktur Folder
legged-robot/
│
├── main.py         # Menu interaktif untuk memilih simulasi
├── forwardk.py     # Modul simulasi Forward Kinematics
├── inversek.py     # Modul simulasi Inverse Kinematics
└── README.md       # Dokumentasi proyek
▶️ Cara Menjalankan
Install library
pip install numpy matplotlib
Jalankan program
python main.py
Pilih mode simulasi
1 → Forward Kinematics
2 → Inverse Kinematics
⚙️ Konfigurasi Robot

Robot planar ini memiliki tiga link:

Link	Panjang
L1	8
L2	6
L3	4

Robot bergerak di bidang 2D, sehingga semua posisi dapat divisualisasikan dalam koordinat X-Y.

📐 Forward Kinematics

Forward Kinematics (FK) menghitung posisi akhir robot dari sudut-sudut joint.

Posisi setiap link dihitung secara bertahap dari base → end-effector
Semakin besar sudut joint, semakin besar perubahan posisi end-effector
Hasil FK divisualisasikan dalam animasi robot bergerak

💡 Intuisi: FK menjawab pertanyaan: “Jika aku memutar sendi ini sekian derajat, di mana ujung robot berada?”

📐 Inverse Kinematics (Pendekatan Geometri)

Inverse Kinematics (IK) menghitung sudut yang dibutuhkan untuk mencapai target.

Metode yang digunakan: geometric approach (berdasarkan segitiga link).

Langkah-langkah:
Hitung posisi wrist (pergelangan) dengan mengurangi kontribusi link terakhir
Bentuk segitiga menggunakan link L1 dan L2
Gunakan trigonometri untuk mendapatkan sudut joint
Sesuaikan link terakhir agar end-effector mencapai target dengan orientasi tepat

⚡ Kelebihan metode ini: cepat, intuitif, dan stabil untuk robot planar.

📊 Analisis Error

Agar mengetahui akurasi robot, dihitung error posisi:

Error = √((x_target − x_actual)² + (y_target − y_actual)²)
Error kecil → robot mengikuti lintasan target dengan baik
Error besar → terjadi deviasi antara target dan posisi aktual
🧠 Insight

Dari simulasi ini, kita bisa melihat:

Bagaimana FK memetakan sudut joint → posisi akhir
Bagaimana IK menyelesaikan masalah sebaliknya: posisi target → sudut joint
Bagaimana robot mengikuti trajectory target secara real-time
Pentingnya geometric IK untuk robot planar sederhana
