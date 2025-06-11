# Assignment:
#Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value
    
if __name__ == "__main__":
    m = Multiplier(10)
    print("Callable:", callable(m))
    print("Result:", m(5))
