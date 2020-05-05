import json

listOClient = []

client = {
    'id':123,
    'name':'Gary',
}

listOClient.append(client)

with open('people.json', 'w') as file:
    json.dump(listOClient, file)
