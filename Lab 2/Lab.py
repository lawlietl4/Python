import json
import sys
import os

listOClient = []


def __init__(self):
    with open('db.json', 'w+') as file:
         listOClient = []
         json.dump(listOClient,file)


def write(arg1, arg2, arg3, arg4):
    if os.path.exists('db.json'):
        with open('db.json', 'r') as inFile:
            listOClient = json.load(inFile)
    else:
        listOClient = []
    person = {
        'first_name': arg1,
        'last_name': arg2,
        'phone_num': arg3,
        'email': arg4
    }
    listOClient.append(person)
    with open('db.json', 'w') as file:
        json.dump(listOClient, file, indent=4)
    print(f'User {sys.argv[2]} has been added')
    pass


def read(file):
    contents = ""
    lines = file.readlines()
    for line in lines:
        contents += line
    if contents == "":
        print("The file is empty")
    else:
        print(contents)


def search(file):
    entries = json.load(file)
    print(entries)
    for entry in entries:
        if sys.argv[2].lower() == entry['first_name'] or sys.argv[2].lower() == entry['last_name']:
            print(entry)
            break


def delete():
    file = open('db.json','r')
    content = json.loads(file.read())
    file.close()

    for con in content:
        if sys.argv[2].lower() == con['first_name'].lower() or sys.argv[2].lower() == con['last_name'].lower():
            content.remove(con)
            break
    print(f'User {sys.argv[2]} has been deleted')
    file = open('db.json','w')
    file.write(json.dumps(content))
    file.close()


class Lab():
    command = ''
    f = ''
    if len(sys.argv) < 2:
        print("you need to supply arguments -l, -f, -d, and/or -a")
    else:
        command = sys.argv[1]
        if command == '-a':
            write(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        elif command == '-l':
            with open('db.json', 'r') as f:
                read(f)
        elif command == '-f':
            with open('db.json', 'r') as f:
                search(f)
        elif command == '-d':
            delete()
        else:
            print("the arguments supplied do not work")
