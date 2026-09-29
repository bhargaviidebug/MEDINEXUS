class Patient:
    def __init__(self, pid, name, age, gender, blood, problem):
        self.pid = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.blood = blood
        self.problem = problem
        self.status = "OPD"
        self.history = [problem]


patients = []
id_no = 1001


def register():
    global id_no

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    blood = input("Enter blood group: ")
    problem = input("Enter problem: ")

    p = Patient("P" + str(id_no), name, age, gender, blood, problem)
    patients.append(p)

    print("Patient registered!")
    print("Patient ID:", p.pid)

    id_no += 1


def search():
    pid = input("Enter patient ID: ")

    for p in patients:
        if p.pid == pid:
            print("Name:", p.name)
            print("Age:", p.age)
            print("Blood Group:", p.blood)
            print("Problem:", p.problem)
            print("Status:", p.status)
            return

    print("Patient not found")


def history():
    pid = input("Enter patient ID: ")

    for p in patients:
        if p.pid == pid:
            print("Medical History:")
            for h in p.history:
                print(h)
            return

    print("Patient not found")


def change_status():
    pid = input("Enter patient ID: ")

    for p in patients:
        if p.pid == pid:
            print("1. OPD")
            print("2. Admitted")
            print("3. Discharged")

            ch = input("Enter choice: ")

            if ch == "1":
                p.status = "OPD"
            elif ch == "2":
                p.status = "Admitted"
            elif ch == "3":
                p.status = "Discharged"

            print("Status:", p.status)
            return

    print("Patient not found")


def patient_menu():
    while True:
        print("\n--- PATIENT MANAGEMENT ---")
        print("1. Register")
        print("2. Search")
        print("3. History")
        print("4. Change Status")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            search()

        elif choice == "3":
            history()

        elif choice == "4":
            change_status()

        elif choice == "5":
            break

        else:
            print("Wrong choice")
