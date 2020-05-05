from Models.people import *

peopleApi = People()
peopleList = peopleApi.getPeople()

counter = 1
for person in peopleList:
    print(counter, person['name'])
    counter += 1

print()
id = int(input('enter the id of the person to display: '))

selectedPerson = peopleList[id - 1]
planet = peopleApi.getPlanet(selectedPerson['homeworld'])

print('\nName:', selectedPerson['name'])
print('\nHair color:', selectedPerson['hair_color'])
print('\nEye color:', selectedPerson['eye_color'])
print('Home Planet Name:',planet['name'], '\n')
