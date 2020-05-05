from Models.apiRequest import apiRequest
from datetime import date

request = apiRequest()
progend = False
while(progend == False):
    start = input("what day do you want to start your view? ")
    end = input("what day do you want to end your view? ")
    print("Dates requested:",request.getDate(start, end),'\n')
    print("Daily closing prices:",request.getPrice(),'\n')
    print("Daily percentages:",request.getDatePercent(),'\n')
    request.getTotPercent()
    determination = input("do you wish to continue?\n 1 for yes, 0 for no ")
    if determination == '0':
        progend = True
