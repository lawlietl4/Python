from client import *


class deserializer():
    def parseClientList(self, clientList):
        clients = list()
        for clientDict in clientList:
            client = self.parseClient(clientDict)
            clients.append(client)
        return clients

    def parseClient(self, clientDict):
        client = Client()

        client.id = clientDict['id']
        client.firstName = clientDict['first_name']
        client.lastName = clientDict['last_name']
        client.email = clientDict['email']
        client.timeZone = clientDict['home_time_zone']
        cards = self.parseCardList(clientDict['credit_cards'])
        client.creditCards = cards

        return client

    def parseCardList(self, cardList):
        cards = list()
        for cardDict in cardList:
            card = self.parseCard(cardDict)
            cards.append(card)
        return cards

    def parseCard(self, cardDict):
        card = creditCard()
        try:
            card.authorizer = cardDict['authorizer']
            card.expirationDate = cardDict['expiration_date']
            card.cardNum = cardDict['card_number']
            card.balance = cardDict['balance']
        except:
            print(cardDict)
        return card
