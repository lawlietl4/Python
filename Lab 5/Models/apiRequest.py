from time import mktime, strptime, strftime
from datetime import date, datetime, timedelta
import statistics


import requests




class apiRequest:
    def __init__(self):
        self.url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
        self.dateList = list()
        self.percentList = list()
        self.priceList = list()

    def getPrice(self):
        self.dateList = list()
        self.response = requests.get(self.url).json()
        # print(self.url)
        for value in self.response['bpi'].items():
            keyValueStr = value
            self.priceList.append(keyValueStr)
        return self.priceList

    def getDatePercent(self):
        # percentList = list()
        yesterday = None
        # print(self.dateList)
        for today in self.priceList:
            if yesterday == None:
                percentage = 0
            else:
                percentage = 100 - int((yesterday[1] / today[1]) * 100)
                pass
            self.percentList.append(percentage)
            # print(today)
            yesterday = today
        return self.percentList

    def getDate(self, dateStart, dateEnd):
        self.dateList = list()
        # percentList = list()
        start = strptime(dateStart, "%m/%d/%Y")
        end = strptime(dateEnd, "%m/%d/%Y")
        begin, ending = mktime(start), mktime(end)
        if timedelta(seconds=ending-begin) > timedelta(days=45) or ending-begin < 0:
            print("your input was invalid")
        else:
            d1, d2 = strftime("%Y-%m-%d", start), strftime("%Y-%m-%d", end)
            self.url = f"https://api.coindesk.com/v1/bpi/historical/close.json?start={d1}&end={d2}"
            responses = requests.get(self.url).json()
        return dateStart,dateEnd

    def getTotPercent(self):
        percents = self.percentList
        maxList = list()
        for price in self.priceList:
            maxList.append(price[1])
        sumTot = sum(percents)
        meanNum = statistics.mean(maxList)
        maximum = max(maxList)
        minimum = min(maxList)
        print(f"Percentage overrall: {sumTot}%")
        print(f"Average Closing price: ${meanNum}")
        print(f"Maximum Price: ${maximum:.2f}")
        print(f"Minimum: ${minimum:.2f}")
        print(self.response['disclaimer'])
