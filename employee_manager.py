import pickle

#The Classes
class Employee:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.position = ""
        self.manager = ""   # manager ID
        self.phone = ""
        self.email = ""
        self.salary = 0.0

    def add_emp(self):
        self.id = input("Enter employee ID: ")
        self.name = input("Enter employee name: ")
        self.position = input("Enter employee position: ")
        self.manager = input("Enter employee manager ID: ")
        self.phone = input("Enter employee phone: ")
        self.email = input("Enter employee email: ")
        try:
            self.salary = float(input("Enter employee salary: "))
        except ValueError:
            print("Invalid salary, set to 0.")
            self.salary = 0.0

    def display_emp(self):
        print("Employee ID: " + self.id)
        print("Employee Name: " + self.name)
        print("Employee Position: " + self.position)
        print("Employee Manager: " + self.manager)
        print("Employee Phone: " + self.phone)
        print("Employee Email: " + self.email)
        print("Employee Salary: " + str(self.salary))


class Manager:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.workers = []   # list of employee IDs
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
            print("That employee does not report to this manager.")
            return False
        emp.position = new_position
        return True

    def give_raise(self, emp, percent):
        """Give one of this manager's workers a percentage pay raise."""
        if emp.id not in self.workers:
            print("That employee does not report to this manager.")
            return False
        emp.salary = round(emp.salary * (1 + percent / 100), 2)
        return True


class Company:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.CEO = ""
        self.email = ""
        self.phone = ""
        self.address = ""
        self.managers = []    # list of manager IDs
        self.employees = []   # list of employee IDs

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


# ---------------------------------------------------------------- Helpers
MANAGER_FILE = "manager.txt"
EMPLOYEE_FILE = "employee.txt"
COMPANY_FILE = "company.txt"


def load_all(filename):
    """Read every pickled object stored in a file."""
    items = []
    try:
        with open(filename, "rb") as f:
            while True:
                try:
                    items.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return items


def save_all(filename, items):
    """Overwrite a file with the given list of objects."""
    with open(filename, "wb") as f:
        for item in items:
            pickle.dump(item, f)


def find_by_id(items, item_id):
    for item in items:
        if item.id == item_id:
            return item
    return None


# ---------------------------------------------------------------- Main code
while True:
    print()
    print("1.Add Manager")
    print("2.Add Employee")
    print("3.Add Company")
    print("4.Assign Manager to Company")
    print("5.Assign Employee to Company")
    print("6.Display Employees of Manager")
    print("7.Pay Raise for Employee")
    print("8.Promote Employee")
    print("9.Delete Manager")
    print("10.Delete Employee")
    print("11.Delete Company")
    print("12.Display Company")
    print("0.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        m = Manager()
        m.add_manager()
        with open(MANAGER_FILE, "ab") as f:
            pickle.dump(m, f)

    elif choice == "2":
        e = Employee()
        e.add_emp()
        with open(EMPLOYEE_FILE, "ab") as f:
            pickle.dump(e, f)
        # Link the new employee to their manager, if that manager exists
        managers = load_all(MANAGER_FILE)
        mgr = find_by_id(managers, e.manager)
        if mgr:
            if e.id not in mgr.workers:
                mgr.workers.append(e.id)
            save_all(MANAGER_FILE, managers)
        elif e.manager:
            print("Note: no manager with that ID yet.")

    elif choice == "3":
        c = Company()
        c.add_company()
        with open(COMPANY_FILE, "ab") as f:
            pickle.dump(c, f)

    elif choice == "4":
        companies = load_all(COMPANY_FILE)
        managers = load_all(MANAGER_FILE)
        comp = find_by_id(companies, input("Enter company ID: "))
        mgr = find_by_id(managers, input("Enter manager ID: "))
        if comp and mgr:
            if mgr.id not in comp.managers:
                comp.managers.append(mgr.id)
            save_all(COMPANY_FILE, companies)
            print("Manager assigned to company.")
        else:
            print("Company or manager not found.")

    elif choice == "5":
        companies = load_all(COMPANY_FILE)
        employees = load_all(EMPLOYEE_FILE)
        comp = find_by_id(companies, input("Enter company ID: "))
        emp = find_by_id(employees, input("Enter employee ID: "))
        if comp and emp:
            if emp.id not in comp.employees:
                comp.employees.append(emp.id)
            save_all(COMPANY_FILE, companies)
            print("Employee assigned to company.")
        else:
            print("Company or employee not found.")

    elif choice == "6":
        managers = load_all(MANAGER_FILE)
        employees = load_all(EMPLOYEE_FILE)
        mgr = find_by_id(managers, input("Enter manager ID: "))
        if mgr:
            mgr.display_manager()
            print("--- Employees ---")
            found = False
            for emp in employees:
                if emp.id in mgr.workers:
                    print()
                    emp.display_emp()
                    found = True
            if not found:
                print("This manager has no employees.")
        else:
            print("Manager not found.")

    elif choice == "7":
        managers = load_all(MANAGER_FILE)
        employees = load_all(EMPLOYEE_FILE)
        mgr = find_by_id(managers, input("Enter manager ID: "))
        emp = find_by_id(employees, input("Enter employee ID: "))
        if mgr and emp:
            try:
                percent = float(input("Enter raise percentage: "))
            except ValueError:
                print("Please enter a number.")
            else:
                if mgr.give_raise(emp, percent):
                    save_all(EMPLOYEE_FILE, employees)
                    print("New salary: " + str(emp.salary))
        else:
            print("Manager or employee not found.")

    elif choice == "8":
        managers = load_all(MANAGER_FILE)
        employees = load_all(EMPLOYEE_FILE)
        mgr = find_by_id(managers, input("Enter manager ID: "))
        emp = find_by_id(employees, input("Enter employee ID: "))
        if mgr and emp:
            new_pos = input("Enter new position: ")
            if mgr.promote_emp(emp, new_pos):
                save_all(EMPLOYEE_FILE, employees)
                print("Employee promoted.")
        else:
            print("Manager or employee not found.")

    elif choice == "12":
        companies = load_all(COMPANY_FILE)
        comp = find_by_id(companies, input("Enter company ID: "))
        if comp:
            comp.display_company()
        else:
            print("Company not found.")

    elif choice == "9":
        managers = load_all(MANAGER_FILE)
        employees = load_all(EMPLOYEE_FILE)
        companies = load_all(COMPANY_FILE)
        mgr_id = input("Enter manager ID to delete: ")
        if find_by_id(managers, mgr_id):
            managers = [m for m in managers if m.id != mgr_id]
            for emp in employees:           # employees lose this manager
                if emp.manager == mgr_id:
                    emp.manager = ""
            for comp in companies:          # remove from companies
                if mgr_id in comp.managers:
                    comp.managers.remove(mgr_id)
            save_all(MANAGER_FILE, managers)
            save_all(EMPLOYEE_FILE, employees)
            save_all(COMPANY_FILE, companies)
            print("Manager deleted.")
        else:
            print("Manager not found.")

    elif choice == "10":
        managers = load_all(MANAGER_FILE)
        employees = load_all(EMPLOYEE_FILE)
        companies = load_all(COMPANY_FILE)
        emp_id = input("Enter employee ID to delete: ")
        if find_by_id(employees, emp_id):
            employees = [e for e in employees if e.id != emp_id]
            for mgr in managers:
                if emp_id in mgr.workers:
                    mgr.workers.remove(emp_id)
            for comp in companies:
                if emp_id in comp.employees:
                    comp.employees.remove(emp_id)
            save_all(MANAGER_FILE, managers)
            save_all(EMPLOYEE_FILE, employees)
            save_all(COMPANY_FILE, companies)
            print("Employee deleted.")
        else:
            print("Employee not found.")

    elif choice == "11":
        companies = load_all(COMPANY_FILE)
        comp_id = input("Enter company ID to delete: ")
        if find_by_id(companies, comp_id):
            companies = [c for c in companies if c.id != comp_id]
            save_all(COMPANY_FILE, companies)
            print("Company deleted.")
        else:
            print("Company not found.")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid input")
