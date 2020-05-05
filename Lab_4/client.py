class Client():
    def __init__(self):
        self.id = None
        self.firstName = None
        self.lastName = None
        self.email = None
        self.timeZone = None
        self.creditCards = list()


class creditCard():
    def __init__(self):
        self.authorizer = None
        self.cardNum = None
        self.expirationDate = None
        self.balance = None
