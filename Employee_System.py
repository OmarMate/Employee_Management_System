import pickle
class Employee:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.position = ""
        self.manager = ""
        self.phone = ""
        self.email = ""
    def add_emp(self):
        self.id = input("Enter employee ID: ")
        self.name = input("Enter employee name: ")
        self.position = input("Enter employee position: ")
        self.manager = input("Enter employee manager: ")
        self.phone = input("Enter employee phone: ")
        self.email = input("Enter employee email: ")

    def display_emp(self):
        print("Employee ID: " + self.id)
        print("Employee Name: " + self.name)
        print("Employee Position: " + self.position)
        print("Employee Manager: " + self.manager)
        print("Employee Phone: " + self.phone)
        print("Employee Email: " + self.email)
class Manager:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.workers = []
        self.phone = ""
        self.email = ""
        self.address = ""
    def add_manager(self):
        self.id = input("Enter manager ID: ")
        self.name = input("Enter manager name: ")
        self.phone = input("Enter manager phone: ")
        self.email = input("Enter manager email: ")
        self.address = input("Enter manager address: ")
    def display_manager(self):
        print("Manager ID: " + self.id)
        print("Manager Name: " + self.name)
        print("Manager Workers: " + ", ".join(self.workers))
        print("Manager Phone: " + self.phone)
        print("Manager Email: " + self.email)
        print("Manager Address: " + self.address)
    def promote_emp(self, emp, new_position):
        if emp.id not in self.workers:
            print("That employee does not report to this manager")
        emp.position = new_position
    def give_raise(self, emp, percent):
        if emp.id not in self.workers:
            print("That employee does not report to this manager")
        emp.salary = round(emp.salary * (1 + percent / 100), 2)
class Company:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.CEO = ""
        self.email = ""
        self.phone = ""
        self.address = ""
        self.managers = []
        self.employees = []
    def add_company(self):
        self.id = input("Enter company ID: ")
        self.name = input("Enter company name: ")
        self.CEO = input("Enter company CEO: ")
        self.email = input("Enter company email: ")
        self.phone = input("Enter company phone: ")
        self.address = input("Enter company address: ")
    def display_company(self):
        print("Company ID: " + self.id)
        print("Company Name: " + self.name)
        print("CEO: " + self.CEO)
        print("Company Email: " + self.email)
        print("Company Phone: " + self.phone)
        print("Company Address: " + self.address)
        print("Company Managers: " + ", ".join(self.managers))
        print("Company Employees: " + ", ".join(self.employees))

    def load_data(fname):
        try:
            file = open(fname, "rb")
            data = pickle.load(file)
            file.close()
            return data
        except FileNotFoundError:
            return []

    def save_data(fname, data):
        file = open(fname, "wb")
        pickle.dump(data, file)
        file.close()

def find_customer(, cid):
    for c in customers:
        if c.cid == cid:
            return c

def find_card(cards, card_no):
    for card in cards:
        if card.card_no == card_no:
            return card
customers = load_data("myCustomers.txt")
cards = load_data("myCards.txt")
manager_file = "manager.txt"
employee_file = "employee.txt"
company_file = "company.txt"

def load_all(filename):
    items = []
    try:
        with open(filename, "r") as f:
            while True:
                try:
                    items.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return items
    def
while True:
    print("1.Add Manager")
    print("2.Add Employee")
    print("3.Add Company")
    print("4.Assign Manager to Company")
    print("5.Assign Employee to Company")
    print("6.Display Employee to Manager")
    print("7. Pay raise for Employee")
    print("7.Promote Employee")
    print("9.Delete Manager")
    print("10.Delete Employee")
    print("11.Delete Company")
    print("10.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        m = Manager()
        m.add_manager()
        file1 = open("manager.txt", "ab")
        pickle.dump(m, file1)
        file1.close()
    elif choice == "2":
        e = Employee()
        e.add_emp()
        file2 = open("employee.txt", "ab")
        pickle.dump(e, file2)
        file2.close()
    elif choice == "3":
        c = Company()
        c.add_company()
        file3 = open("company.txt", "ab")
        pickle.dump(c, file3)
        file3.close()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid input")
