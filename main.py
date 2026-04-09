from forward_kinematics import run_forward
from inverse_kinematics import run_inverse


def main_menu():
    print("\n=== 3-LINK ROBOT SIMULATION SYSTEM ===")
    print("Pilih mode simulasi:")
    print("[1] Forward Kinematics (Joint Motion)")
    print("[2] Inverse Kinematics (Trajectory Tracking)")
    print("[0] Keluar")


def run_simulation():
    while True:
        main_menu()
        choice = input("Masukkan pilihan: ").strip()

        if choice == "1":
            print("\nMenjalankan Forward Kinematics...\n")
            run_forward()

        elif choice == "2":
            print("\nMenjalankan Inverse Kinematics...\n")
            run_inverse()

        elif choice == "0":
            print("\nProgram selesai.")
            break

        else:
            print("\n[ERROR] Input tidak valid, coba lagi!\n")


if __name__ == "__main__":
    run_simulation()