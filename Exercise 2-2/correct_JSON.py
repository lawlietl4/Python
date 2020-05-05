import json


def count(clients):
    clientCount = 0
    for client in clients:
        clientCount += 1
    return clientCount, 'total users'
    pass


def first_names(clients):
    name_list = []
    for client in clients:
        first_name = client['first_name']
        name_list.append(first_name)
    return name_list
    pass


def full_name(clients):
    name_list = []
    for client in clients:
        full_name = f"{client['first_name']} {client['last_name']}"
        name_list.append(full_name)
    return name_list
    pass


def full_names_r(clients):
    r_list = []
    r_count = 0
    for client in clients:
        first_name = client['first_name']
        if str(first_name).startswith('R'):
            full_name = f"{client['first_name']}, {client['last_name']}"
            r_count += 1
            r_list.append(full_name)
    return f'{r_list} {r_count} names that start with R'
    pass


def negative_bal(clients):
    neg_count = 0
    negs = list()
    name_list = list()
    for client in clients:
        full_name = client['first_name'], client['last_name']
        for card in client['credit_cards']:
            if card['balance'] < 0:
                negs.append((full_name, card['card_number'], card["balance"]))
                neg_count += 1
        statement = f'{negs} {neg_count} users with negative balance'
    return statement
    pass


with open('bank_clients.json', 'r') as data:
    clients = json.load(data)


print(count(clients), '\n')
print(first_names(clients), '\n')
print(full_name(clients), '\n')
print(full_names_r(clients), '\n')
print(negative_bal(clients), '\n')
