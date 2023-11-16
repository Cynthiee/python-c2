class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print('Personal Details')
        print("")
        print('Account name ', self.name)
        print('Age ', self.age)
        print('Gender', self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposite(self, amount):
        self.amount = amount
        self.balance += amount
        print('Account balance has been updated ', self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print('Insufficient funds ', self.balance)
        else:
            self.balance = self.balance - self.amount
            print('Account balance has been updated ', self.balance)

    def view_balance(self):
        self.show_details()
        print('Account balance is ', self.balance)

John = Bank('Ada', 23, 'Female')
John.deposite(67)
# John = User('John', 21, 'Male')
# John.show_details()
# John = Bank('John', 21, 'Male')
# John.name
# John.age
# John.gender
