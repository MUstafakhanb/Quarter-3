# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "KK Bank"

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

b1:Bank = Bank()
print(b1.bank_name)
b2:Bank = Bank()
print(b2.bank_name)
Bank.change_bank_name("KKR Bank")
print(b1.bank_name)
print(b2.bank_name)