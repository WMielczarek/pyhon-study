import json
import os.path

def loadJson(filename):
    if os.path.isfile(filename + '.json'):
        with open(filename + '.json') as f:
            data = json.load(f)
        return data
    else:
        createExample(myString)
        with open(filename='.json') as f:
            data = json.load(f)
        return data

def saveJson(fileName, data):
    with open(fileName + '.json', 'w') as f:
        json.dump(data, f, indent=2)
    return

def createExample(myString):
    data = json.load(myString)
    saveJson('oferty', data)





myString = '''{
    "OFFERTS": [
        {"ID": "1",
         "Title": "Wyjazd",
         "Driver": "Henryk",
         "Departure": "Szczecin",
         "Destination": "Zielona Góra",
         "Departure date": "12/06/2018",
         "Departure time": "11.00",
         "Added": "25/05/2018",
         "Rating": "4"
         },
        {"ID": "2",
         "Title": "Odjazd",
         "Driver": "Wojtek",
         "Departure": "Wroclaw",
         "Destination": "Warszawa",
         "Departure date": "12/06/2018",
         "Departure time": "13.00",
         "Added": "26/05/2018",
         "Rating": "4"
        },
        {"ID": "3",
         "Title": "Ruszamy",
         "Driver": "Katarzyna",
         "Departure": "Gdynia",
         "Destination": "Międzyzdroje",
         "Departure date": "11/07/2018",
         "Departure time": "14.00",
         "Added": "25/06/2018",
         "Rating": "6"
         },
        {"ID": "4",
         "Title": "Jedzmy",
         "Driver": "KrzysiekK",
         "Departure": "Poznan",
         "Destination": "Wroclaw",
         "Departure date": "15/06/2018",
         "Departure time": "10.00",
         "Added": "22/05/2018",
         "Rating": "6"
         }   
    ]
}'''
