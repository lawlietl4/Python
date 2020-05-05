import json
import bcrypt

with open('logins.json') as logins:
    usrs = json.load(logins)

usr = input('Username: ')
pwd = input('Password: ').encode('utf-8')

if usr in usrs:
    if bcrypt.checkpw(pwd, usrs[usr].encode('utf-8')):
        print('Login successful')
    else:
        print('Login failed')
else:
    salt = bcrypt.gensalt()
    usrs[usr] = bcrypt.hashpw(pwd, salt).decode('utf-8')
    with open('logins.json', 'w') as logins:
        json.dump(usrs, logins)
    print('Created new user ' + usr)
