from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()


# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f"Department {name} not found")


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f"Department {id_} not found")


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f"Success: {department}")
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f"Success: {department}")
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f"Department {id_} not found")


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f"Department {id_} deleted")
    else:
        print(f"Department {id_} not found")


# You'll implement the employee functions in the lab


def list_employees():
    pass
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    pass
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f"Employee {name} not found")


def find_employee_by_id():
    pass
    id = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id)
    print(employee) if employee else print(f"Employee {id} not found")


def create_employee():
    pass
    name = input("Enter employee's name: ")
    job_title = input("Enter employee's job title: ")
    department_id = int(input("Enter employee's department id: "))
    try:
        employee = Employee.create(name, job_title, department_id)
        print(f"Success: {employee}")
    except Exception as exc:
        print("Error creating employee: ", exc)


def update_employee():
    pass
    id = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id)
    if employee:
        try:
            name = input("Enter new employee's name: ")
            employee._name = name
            job_title = input("Enter new employee's job title: ")
            employee._job_title = job_title
            department_id = int(input("Enter new employee's department id: "))
            employee._department_id = department_id
            employee.update()
            print(f"{employee.name} has successfully been updated")
        except Exception as exc:
            print(f"Error updating employee: ", exc)
    else:
        print(f"Employee {id} not found")


def delete_employee():
    pass
    id = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id):
        try:
            employee.delete()
            print(f"{employee.name} has been successfully deleted")
        except Exception as exc:
            print(f"Error deleting {employee._name}", exc)
    else:
        print(f"Employee {id} not found")


def list_department_employees():
    pass
    id = input("Enter the department's id: ")
    if department := Department.find_by_id(id):
        try:
            employees = department.employees()
            for employee in employees:
                print(employee)
        except Exception as exc:
            print(f"Error getting employees under {department._name} department", exc)
    else:
        print(f"Department {id} not found")