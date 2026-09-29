admissions = []
medicines = []
bills = []


def hospital_menu():

    while True:

        print("\n--- HOSPITAL SERVICES ---")
        print("1. Admit Patient")
        print("2. Add Medicine")
        print("3. Make Bill")
        print("4. Show Admissions")
        print("5. Show Bills")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            patient = input("Enter patient ID: ")
            room = input("Enter room number: ")

            admissions.append([patient, room])

            print("Patient admitted")

        elif choice == "2":

            medicine = input("Enter medicine name: ")
            quantity = input("Enter quantity: ")

            medicines.append([medicine, quantity])

            print("Medicine added")

        elif choice == "3":

            patient = input("Enter patient ID: ")
            amount = input("Enter bill amount: ")

            bills.append([patient, amount])

            print("Bill created")
            print("Amount:", amount)

        elif choice == "4":

            print("\nAdmissions")

            if len(admissions) == 0:
                print("No patients admitted")

            for a in admissions:
                print("Patient:", a[0], "Room:", a[1])

        elif choice == "5":

            print("\nBills")

            if len(bills) == 0:
                print("No bills")

            for b in bills:
                print("Patient:", b[0], "Amount:", b[1])

        elif choice == "6":

            print("Hospital section closed")
            break

        else:

            print("Wrong choice")
