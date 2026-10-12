
employees = {
    101: {"name": "Ram", "department": "IT", "salary": 30000},
    102: {"name": "Sita", "department": "HR", "salary": 35000},
    103: {"name": "Hari", "department": "Finance", "salary": 40000},
    104: {"name": "Gita", "department": "Marketing", "salary": 32000},
    105: {"name": "Shyam", "department": "IT", "salary": 45000}
}

def find_employee(emp_id):
    try:
        return employees[emp_id]
    except KeyError:
        print("Employee ID does not exist!")
        return None

def yearly_salary(salary):
    return salary * 12

def increase_salary(employee, percentage):
    old_salary = employee["salary"]
    increase = old_salary * percentage / 100
    new_salary = old_salary + increase
    employee["salary"] = new_salary

    print("\n===== EMPLOYEE SALARY DETAILS =====")
    print("Employee Name:", employee["name"])
    print("Department:", employee["department"])
    print("Old Salary:", old_salary)
    print("Salary Increase:", percentage, "%")
    print("New Salary:", new_salary)
    print("Yearly Salary:", yearly_salary(new_salary))

try:
    emp_id = int(input("Enter employee ID: "))

    employee = find_employee(emp_id)

    if employee is not None:
        percentage = float(input("Enter salary increase percentage: "))

        if percentage < 0:
            print("Percentage cannot be negative!")
        else:
            increase_salary(employee, percentage)

except ValueError:
    print("Invalid input! Please enter a valid number.")
