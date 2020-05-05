import json


with open("bank_clients.json", "r") as file:
    newList = []
    fullNameList = []
    rList = []
    negativeList = []
    balanceList = []
    cardNumList = []
    nameList = []
    clientCount = 0
    clientCountA = 0
    clientCountB = 0
    client = json.load(file)
    for clients in client:
        clientCount += 1
    for clients in client:
        first_name = clients["first_name"]
        newList.append(first_name)
    for clients in client:
        first_name = clients["first_name"]
        last_name = clients["last_name"]
        full_name = first_name, last_name
        fullNameList.append(full_name)
    for clients in client:
        first_name = clients["first_name"]
        last_name = clients["last_name"]
        if str(first_name).startswith("R"):
            full_name = first_name, last_name
            rList.append(full_name)
            clientCountA += 1
    for clients in client:
        for card in client['credit_cards']:
            if card['balance'] < 0:
                pass
file.close()

print(clientCount, "users\n")
print(newList, "\n")
print(fullNameList, "\n")
print(rList, clientCountA, "first names that begin with R", "\n")
