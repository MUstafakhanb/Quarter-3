# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

from collections.abc import Iterable


class logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
       print("Logger object destroyed.")

log:logger = logger()
print(log)

print("Mustafa Qaiser")