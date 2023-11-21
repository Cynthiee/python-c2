class Pymoni:
    bank = 'Pymoni'
    def __init__(self, name, acct_number, inquiry, balance):
        self.name = name
        self.acct_number = acct_number
        # self.address = address
        self.balance = balance
        self.inquiry = inquiry

    def details(self):
        self.name = input('Enter you account name: ')
        self.acct_number = input('Enter your account number: ')
        # self.inquiry = input('Choose and option: Inquiry? Deposit? or Withdrawal? ')
        if len(self.acct_number) == 10 and self.acct_number.isdigit():
            print(f'Hello {self.name}, WELCOME TO PYMONI\nYour account number is {self.acct_number}')
        else:
            print('Invalid Account number!!!')
            exit()
                
    def balances(self):
        self.balance = 0
        print(f'Your account bal: ${self.balance:2f}')
        
    def deposit(self, amount):
        self.amount = amount
        self.amount = int(input('Enter amount '))
        self.balance += self.amount
        print(self.balance)
        if self.balance > self.balance:
            print(f'You just topped up! {self.balance}')
        else:
            print('Deposit failed')


deta = Pymoni('Abiagil', 123, 'Go', 1)
deta.details()
deta.balances()
deta.deposit(9)

# melody = Pymoni('Ada', 647, 48, 9)
