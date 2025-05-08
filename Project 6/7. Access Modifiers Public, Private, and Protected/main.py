# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self.salary = salary
        self.ssn = ssn

emp1 : Employee = Employee("Mustafa Qaiser",50000,"123-456-789")
print(emp1.name)
print(emp1.salary)
print(emp1.ssn)