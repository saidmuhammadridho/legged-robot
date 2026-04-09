from forward_kinematics import animate_robot
from inverse_kinematics import animate_inverse_robot

def show_menu():
    print("\n=== 3-Link Robot Simulator ===")
    print("Silakan pilih mode simulasi:")
    print("  1 - Forward Kinematics (Gerakan Joint)")
    print("  2 - Inverse Kinematics (Pelacakan Trajectory)")
    print("  0 - Keluar Program")

def start_simulator():
    while True:
        show_menu()
        user_input = input("Masukkan pilihan Anda: ").strip()

        if user_input == "1":
            print("\n>>> Memulai simulasi Forward Kinematics...\n")
            animate_robot()

        elif user_input == "2":
            print("\n>>> Memulai simulasi Inverse Kinematics...\n")
            animate_inverse_robot()

        elif user_input == "0":
            print("\nTerima kasih! Program ditutup.")
            break

        else:
            print("\n[PERINGATAN] Input tidak dikenali, silakan coba lagi.\n")

if __name__ == "__main__":
    start_simulator()