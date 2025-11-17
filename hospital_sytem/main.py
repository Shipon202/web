class HospitalManagementSystem:
    def __init__(self):
        self.patients = []  # List to store patient details
        self.doctors = {
            "professor": [{"name": "Dr. Smith", "specialization": "Cardiology"}, {"name": "Dr. Johnson", "specialization": "Neurology"}],
            "intern": [{"name": "Dr. Davis", "specialization": "General Medicine"}, {"name": "Dr. Taylor", "specialization": "Pediatrics"}],
        }
        self.appointments = []  # List of appointments
        self.pharmacy_inventory = {"Paracetamol": 50, "Amoxicillin": 30, "Insulin": 20}
        self.lab_tests = {"Blood Test": 500, "MRI": 5000, "X-Ray": 2000}
        self.beds = {"general": 10, "ICU": 5}  # Beds available
        self.financial_records = []  # List of financial transactions

    # Patient Management
    def add_patient(self):
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        condition = input("Enter patient's condition: ")

        # Select bed type
        print("\nAvailable Beds:")
        for bed_type, count in self.beds.items():
            print(f"{bed_type.capitalize()}: {count} beds available")

        bed_type = input("Enter bed type for the patient (general/ICU): ").lower()
        if self.beds.get(bed_type, 0) > 0:
            self.beds[bed_type] -= 1
            self.patients.append({
                "name": name,
                "age": age,
                "gender": gender,
                "condition": condition,
                "bed_type": bed_type.capitalize()
            })
            print(f"Patient {name} added successfully and allocated a {bed_type.capitalize()} bed.")
        else:
            print(f"Sorry, no {bed_type} beds available. Patient {name} was not admitted.")

    def view_patients(self):
        if not self.patients:
            print("No patients found.")
        else:
            print("Patient List:")
            for patient in self.patients:
                print(f"Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, Condition: {patient['condition']}, Bed: {patient.get('bed_type', 'None')}")

    # Doctor and Appointment Management
    def book_appointment(self):
        print("Available Doctors:")
        for doctor_type, doctors in self.doctors.items():
            print(f"\n{doctor_type.capitalize()} Doctors:")
            for i, doctor in enumerate(doctors, start=1):
                print(f"  {i}. {doctor['name']} ({doctor['specialization']})")
        doctor_type = input("Enter doctor type (professor/intern): ").lower()
        doctor_index = int(input(f"Choose doctor (1-{len(self.doctors[doctor_type])}): ")) - 1
        patient_name = input("Enter patient's name for the appointment: ")
        doctor_name = self.doctors[doctor_type][doctor_index]["name"]
        self.appointments.append({"patient": patient_name, "doctor": doctor_name})
        print(f"Appointment booked for {patient_name} with {doctor_name}.")

    def view_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            print("Scheduled Appointments:")
            for app in self.appointments:
                print(f"Patient: {app['patient']}, Doctor: {app['doctor']}")

    # Pharmacy Management
    def manage_pharmacy(self):
        print("Pharmacy Inventory:")
        for medicine, stock in self.pharmacy_inventory.items():
            print(f"{medicine}: {stock} units")
        medicine = input("Enter medicine name to update stock: ")
        quantity = int(input("Enter quantity to add: "))
        self.pharmacy_inventory[medicine] = self.pharmacy_inventory.get(medicine, 0) + quantity
        print(f"{medicine} stock updated.")

    # Laboratory Management
    def manage_lab(self):
        print("Available Lab Tests:")
        for test, cost in self.lab_tests.items():
            print(f"{test}: {cost} INR")
        patient_name = input("Enter patient name for the lab test: ")
        test = input("Enter the lab test name: ")
        if test in self.lab_tests:
            self.financial_records.append({"patient": patient_name, "type": "Lab Test", "amount": self.lab_tests[test]})
            print(f"{test} booked for {patient_name}.")
        else:
            print("Invalid test name.")

    # Bed and Inpatient Management
    def manage_beds(self):
        print("Available Beds:")
        for bed_type, count in self.beds.items():
            print(f"{bed_type.capitalize()}: {count} beds available")
        bed_type = input("Enter bed type (general/ICU): ").lower()
        if self.beds.get(bed_type, 0) > 0:
            self.beds[bed_type] -= 1
            print(f"{bed_type.capitalize()} bed allocated.")
        else:
            print(f"No {bed_type} beds available.")

    # Financial Management
    def view_financials(self):
        print("Financial Transactions:")
        if not self.financial_records:
            print("No transactions yet.")
        else:
            for record in self.financial_records:
                print(f"Patient: {record['patient']}, Type: {record['type']}, Amount: {record['amount']} INR")

    # Main Menu
    def main_menu(self):
        while True:
            print("\n--- Hospital Management System ---")
            print("1. Add Patient")
            print("2. View Patients")
            print("3. Book Appointment")
            print("4. View Appointments")
            print("5. Manage Pharmacy")
            print("6. Manage Laboratory")
            print("7. Manage Beds")
            print("8. View Financial Transactions")
            print("9. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.view_patients()
            elif choice == "3":
                self.book_appointment()
            elif choice == "4":
                self.view_appointments()
            elif choice == "5":
                self.manage_pharmacy()
            elif choice == "6":
                self.manage_lab()
            elif choice == "7":
                self.manage_beds()
            elif choice == "8":
                self.view_financials()
            elif choice == "9":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")


# Run the Hospital Management System
if __name__ == "__main__":
    hms = HospitalManagementSystem()
    hms.main_menu()
