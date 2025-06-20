#Assignment:
#Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < 0:
            raise StopIteration
        value = self.start
        self.start -= 1
        return value
    
cd = Countdown(5)
for number in cd:
    print(number)
