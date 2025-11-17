class HospitalManagmentSytem:
    def __init__(self):
        self.patients =[]
        self.doctors = {
            "professor": [{"name": "Dr.smith", "specialization": "Cardiology"}, {"name": "Dr.Johson", "specialization": "Neurology"} ],
            "intern": [{"name": "Dr.Davis", "specialization": "Cardiology"},{"name": "Dr.Taylor", "specialization": "Medicine"}]
        }
        self.appointments = []
        self.pharmacy_inventory = {"paracetamol" : 50, "Amoxicilin": 30, "Insulin": 20}
        self.lab_test = {"Blood_Test": 500, "MRI": 5000, "X-ray": 2000}
        self.beds = {"General": 10, "ICU": 5}
        self.financial = []
    def add_patient(self):
        name = input("Enter patient name : ")
        age = float(input("Enter patitent ages : "))
        gender = input("Enter patient gender : ")
        condition = input("Enter patient problems : ")
        print("Available beds: ")
        for bed_type, count in self.beds.items():
            print(f"{bed_type.capitalize()}: {count} beds available")

    def view_patient(self):
        pass
    def book_appointment(self):
        pass
    def manage_pharmacy(self):
        pass
    def manage_lab(self):
        pass
    def manage_beds(self):
        pass
    def view_finacials(self):
        pass


    def main_manu(self):
        while True:
            print("---------Hospital Management Sytem---------")
            print("1. Add patient")
            print("2. View patient")
            print("3. Book Appointment")
            print("4. View Appointment")
            print("5. Manage Pharmacy")
            print("6. Manage Laboratoty")
            print("7. Manage Beds")
            print("8. View Financial Transction")
            print("9. Exit")
            choice = input("Enter your choice of number : ")
            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.view_patient
            elif choice == "3":
                self.book_appointment
            elif choice == "4":
                self.view_appointments
            elif choice == "5":
                self.manage_pharmacy
            elif choice == "6":
                self.manage_lab
            elif choice == "7":
                self.manage_beds
            elif choice == "8":
                self.view_finacials
            elif choice == "9":
                print("Exiting the system ")
                break
            else:
                print("Invalid number. Please enter a a valid number")
 
if __name__=="__main__":
    hms = HospitalManagmentSytem()
    hms.main_manu()