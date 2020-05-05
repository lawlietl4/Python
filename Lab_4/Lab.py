import argparse
import json
import sys

import dataModel
import psycopg2
from deserialize import *


model = dataModel.DbCustomer()
connection = psycopg2.connect(host='localhost', port='5432',
                              user='Guest', password='1234', database='banking')
cursor = connection.cursor()
connection.autocommit = True

f = open('bank_clients.json', 'r')
file = json.load(f)
deserializer = deserializer()
clients = deserializer.parseClientList(file)
f.close()

parser = argparse.ArgumentParser()
parser.add_argument('-p', action='store_true', default=False, help=argparse.SUPPRESS)
parser.add_argument('-i', action='store_true',
                    default=True, help=argparse.SUPPRESS)
parser.add_argument('-overdrawn', action='store_true', default=False,
                    help='Returns cards in the database with negative balances')
parser.add_argument('-expired', action='store_true',
                    help='Returns cards that are expired as of today', default=False)
parser.add_argument('-balanceGreaterThan', nargs='?', help='Returns cards with a balance greater than what is inputted')
parser.add_argument('-balanceLessThan',
                    nargs='?', help='Returns cards with a balance less than what is inputted')

args = parser.parse_args()


try:
    if args.i == True:
        model.createTable()
        for client in clients:
            model.insert(client)
            for card in client.creditCards:
                model.insertCard(client.id, card)
except:
    if args.balanceGreaterThan:
        clientDict = dict()
        # parser.parse_args(args.greaterthan)
        searchStatement = f"""
        SELECT banking.last_name, banking.first_name, credit_cards.authorizer, credit_cards.card_number, credit_cards.expiration_date, credit_cards.balance FROM banking INNER JOIN credit_cards ON banking.id_num = credit_cards.client_id WHERE credit_cards.balance > '{args.balanceGreaterThan}';
        """
        cursor.execute(searchStatement)
        results = cursor.fetchall()
        if results == None:
            print('No matching results found')
        for result in results:
            clientDict['first_name'] = result[1]
            clientDict['last_name'] = result[0]
            clientDict['credit_cards'] = dict()
            clientDict['credit_cards']['authorizer'] = result[2]
            clientDict['credit_cards']['card_number'] = result[3]
            clientDict['credit_cards']['expiration_date'] = result[4]
            clientDict['credit_cards']['balance'] = result[5]
            print(clientDict)
    elif args.balanceLessThan:
        clientDict = dict()
        # parser.parse_args(args.lessthan)
        searchStatement = f"""
        SELECT banking.last_name, banking.first_name, credit_cards.authorizer, credit_cards.card_number, credit_cards.expiration_date, credit_cards.balance FROM banking INNER JOIN credit_cards ON banking.id_num = credit_cards.client_id WHERE credit_cards.balance < '{args.balanceLessThan}';
        """
        cursor.execute(searchStatement)
        results = cursor.fetchall()
        if results == None:
            print('No matching results found')
        for result in results:
            clientDict['first_name'] = result[1]
            clientDict['last_name'] = result[0]
            clientDict['credit_cards'] = dict()
            clientDict['credit_cards']['authorizer'] = result[2]
            clientDict['credit_cards']['card_number'] = result[3]
            clientDict['credit_cards']['expiration_date'] = result[4]
            clientDict['credit_cards']['balance'] = result[5]
            print(clientDict)
    elif args.expired:
        clientDict = dict()
        searchTerm = f"""
        SELECT banking.last_name, banking.first_name, credit_cards.authorizer, credit_cards.card_number, credit_cards.expiration_date, credit_cards.balance FROM banking INNER JOIN credit_cards ON banking.id_num = credit_cards.client_id WHERE  CAST(credit_cards.expiration_date as date) <= CAST(localtimestamp as date);
        """
        cursor.execute(searchTerm)
        results = cursor.fetchall()
        if results == None:
            print('No matching results found')
        for result in results:
            clientDict['first_name'] = result[1]
            clientDict['last_name'] = result[0]
            clientDict['credit_cards'] = dict()
            clientDict['credit_cards']['authorizer'] = result[2]
            clientDict['credit_cards']['card_number'] = result[3]
            clientDict['credit_cards']['expiration_date'] = result[4]
            clientDict['credit_cards']['balance'] = result[5]
            print(clientDict)
    elif args.overdrawn:
        clientDict = dict()
        searchTerm = """
        SELECT banking.last_name, banking.first_name, credit_cards.authorizer, credit_cards.card_number, credit_cards.expiration_date, credit_cards.balance FROM banking INNER JOIN credit_cards ON banking.id_num = credit_cards.client_id WHERE credit_cards.balance < 0;
        """
        cursor.execute(searchTerm)
        results = cursor.fetchall()
        if results == None:
            print('No matching results found')
        for result in results:
            clientDict['first_name'] = result[1]
            clientDict['last_name'] = result[0]
            clientDict['credit_cards'] = dict()
            clientDict['credit_cards']['authorizer'] = result[2]
            clientDict['credit_cards']['card_number'] = result[3]
            clientDict['credit_cards']['expiration_date'] = result[4]
            clientDict['credit_cards']['balance'] = result[5]
            print(clientDict)
    else:
        print('No matching results found')
    dropTable = """
            DROP TABLE IF EXISTS banking.local.banking;
            """
    dropTableA = """
            DROP TABLE IF EXISTS banking.local.credit_cards;
            """
    cursor.execute(dropTable)
    cursor.execute(dropTableA)
    connection.close()
