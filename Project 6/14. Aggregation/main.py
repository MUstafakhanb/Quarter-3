# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self,emp_id,name):
        self.emp_id = emp_id
        self.name = name

    def display_info(self):
        print(f'Employee ID: {self.emp_id}, Name: {self.name}')


class Department:
    def __init__(self,dept_name,employee:Employee):
        self.dept_name = dept_name
        self.employee = employee

    def display_department_info(self):
        print(f'Depatment: {self.dept_name}')
        self.employee.display_info()


emp1 = Employee(110, "John")

dept1 = Department("Human Management",emp1)
dept1.display_department_info()

print("\n Accessing employee directly")
emp1.display_info()