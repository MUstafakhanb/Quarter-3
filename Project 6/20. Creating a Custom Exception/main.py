#Assignment:
#Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Invalid age: Must be at least 18.")
    else:
        print("Age is valid. Access granted.")

try:
    age_input = int(input("Enter your age: "))
    check_age(age_input)
except InvalidAgeError as e:
    print("Exception caught:", e)
except ValueError:
    print("Invalid input: Please enter a number.")
