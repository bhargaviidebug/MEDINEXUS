doctors = []
appointments = []


def add_doctor():
    name = input("Doctor name: ")
    dept = input("Department: ")

    doctors.append([name, dept])
    print("Doctor added")


def show_doctors():
    if not doctors:
        print("No doctors yet")
    else:
        for doctor in doctors:
            print("Name:", doctor[0])
            print("Department:", doctor[1])
            print()


def book_appointment():
    patient = input("Patient ID: ")
    doctor = input("Doctor name: ")
    date = input("Date: ")

    appointments.append([patient, doctor, date])
    print("Appointment booked")


def show_appointments():
    if not appointments:
        print("No appointments")
    else:
        for a in appointments:
            print("Patient:", a[0])
            print("Doctor:", a[1])
            print("Date:", a[2])
            print()


def doctor_menu():
    while True:
        print("\n--- DOCTOR MANAGEMENT ---")
        print("1. Add Doctor")
        print("2. Show Doctors")
        print("3. Book Appointment")
        print("4. Show Appointments")
        print("5. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            add_doctor()

        elif ch == "2":
            show_doctors()

        elif ch == "3":
            book_appointment()

        elif ch == "4":
            show_appointments()

        elif ch == "5":
            break

        else:
            print("Invalid choice")
