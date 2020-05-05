from bankAccount import*

balance = 100
accountNum = 981028347890

account = CheckingAccount(accountNum, balance)

# account.__init__
account.withdraw(130)

print(account)
