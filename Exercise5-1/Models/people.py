# -*-coding: utf-8-*-
import requests
from operator import itemgetter


class People:

    def getPeople(self):
        url = 'https://swapi.py4e.com/api/people/'
        people = list()
        data = requests.get(url).json()
        people.extend(data["results"])
        while(data['next'] != None):
            url = data['next']
            data = requests.get(url).json()
            people += data['results']
        return people

    def getPlanet(self, url):
        planet = requests.get(url).json()
        return planet
