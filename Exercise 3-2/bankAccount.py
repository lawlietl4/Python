class BankAccount():
    accountNumber = 0
    balance = 0
    minimum_balance = 25

    def __init__(self, accountNumber, balance):
        self.accountNumber = 981028347890
        self.balance = 100
    pass

    def deposit(self, balance):
        self.balance += balance
    pass

    def withdraw(self, balance):
        if balance > self.balance:
            print("\rYou have insufficient funds\n")
            pass
        else:
            self.balance -= balance
    pass


class CheckingAccount(BankAccount):
    accountNum = 0

    def __init__(self, accountNum, balance):
        BankAccount.balance = 100
        self.accountNum = 785468237443

    def __str__(self):
        return f'Your balance is: ${self.balance}'

    def withdraw(self, balance):
        if self.balance + 25 < balance:
            print(
                f'You cannot withdraw more than 25 dollars over your current account balance: ${BankAccount.balance}')
        else:
            self.balance -= balance
    pass
