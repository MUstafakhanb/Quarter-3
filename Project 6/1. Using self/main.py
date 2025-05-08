# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        return(f'Name: {self.name}, Marks{self.marks}')

student1:Student = Student("MustafaQaiser",94)
student2:Student = Student("Ali Hassam",88)
print("Student 1 Details:",student1.display())
print(student1.name,student1.marks)
print("Student 2 Details:",student2.display())