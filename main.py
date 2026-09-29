from patient_module import patient_menu
from doctor_module import doctor_menu
from hospital_module import hospital_menu


while True:

    print("\n========== MEDINEXUS ==========")
    print("1. Patient Management")
    print("2. Doctor Management")
    print("3. Hospital Services")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        patient_menu()

    elif choice == "2":
        doctor_menu()

    elif choice == "3":
        hospital_menu()

    elif choice == "4":
        print("\nThank you for using MEDINEXUS!")
        break

    else:
        print("\nInvalid choice. Please try again.")
