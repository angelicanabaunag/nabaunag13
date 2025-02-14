
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    def display_employee(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ₱{self.salary:.2f}")


# Creating an employee instance
employee = Employee("Laila Valmorida", "Computer Engineer", 24486)

# Giving the employee a raise
employee.give_raise(5000)

# Displaying employee details
employee.display_employee()
