import sys
import bcrypt
import getpass

from Models.dataModel import *

customer = DbCustomer()
salt = bcrypt.gensalt()
if sys.argv[1] == '-c':
    customer.createTable(
        input('What name do you want to assign to the table? '))

elif sys.argv[1] == '-r':
    table = input('What table do you want to insert to? ')
    first_name = input('what name are you registering? ')
    last_name = input("what's the client's last name? ")
    email = input('The client email ')
    password = getpass.getpass(
        'please enter the password the user will be using ').encode('utf-8')
    hashed = bcrypt.hashpw(password, salt)
    hash_str = hashed.decode('utf-8')
    customer.insert(email, hash_str, first_name, last_name, table)
    print('Writing to database done')

elif sys.argv[1] == '-l':
    password = getpass.getpass('please enter your password ')
    try:
        customer.login(sys.argv[2], password)
    except:
        print(f'Welcome {sys.argv[2]}')
        print('the password you input was incorrect\n the commands that can be used in this program are -r for registering users to the database\n -l for logging into the database')
elif sys.argv[1] == '-d':
    customer.delTable(
        input('What table would you like to drop from the database? '))
elif sys.argv[1] == '-list':
    customer.select(input('What table do you want to list elements from? '))
