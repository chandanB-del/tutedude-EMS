# Employee Management System (EMS)

# Step 1: Initialize employee data
employees = {
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000},
    102: {"name": "Ravi", "age": 30, "department": "IT", "salary": 65000}
}


# Step 2: Main Menu
def main_menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("\nThank you for using the Employee Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Step 3: Add Employee
def add_employee():
    while True:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists. Please enter a unique ID.")
        else:
            break

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = float(input("Enter Employee Salary: "))

    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }

    print("Employee added successfully!")


# Step 4: View All Employees
def view_employees():
    if not employees:
        print("\nNo employees available.")
        return

    print("\n{:<10} {:<15} {:<10} {:<15} {:<10}".format(
        "Emp ID", "Name", "Age", "Department", "Salary"
    ))
    print("-" * 60)

    for emp_id, details in employees.items():
        print("{:<10} {:<15} {:<10} {:<15} {:<10}".format(
            emp_id,
            details["name"],
            details["age"],
            details["department"],
            details["salary"]
        ))


# Step 5: Search Employee by ID
def search_employee():
    emp_id = int(input("Enter Employee ID to search: "))

    if emp_id in employees:
        emp = employees[emp_id]
        print("\nEmployee Details:")
        print(f"Name       : {emp['name']}")
        print(f"Age        : {emp['age']}")
        print(f"Department : {emp['department']}")
        print(f"Salary     : {emp['salary']}")
    else:
        print("Employee not found.")


# Program Execution
if __name__ == "__main__":
    main_menu()