import json

from client import *
from deserialize import *

newFile = open('small_client_list.json', 'w')
file = open('bank_clients.json', 'r')
clientList = json.load(file)

deserializer = deserializer()

clients = deserializer.parseClientList(clientList)

for client in clients:
    print(client.id, client.firstName)
    json.dump(clientList, newFile, indent=4)

# clientString = json.dumps(clients, default= lambda o:o.__dict__, indent = 4)

# print(clientString)
