# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        self.__price = value         

    @price.deleter
    def price(self):
        del self.__price
    
if __name__ == "__main__":
    p = Product(200)
    print(p.price)
    p.price = 150
    print(p.price)
    del p.price
    print(p.price)