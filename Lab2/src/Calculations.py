import math
import csv
import datetime
import glob
import os
#RH - wilgotnosc wzgledna

def getHourFromFileName(fileName):
    (name, data, hour) = fileName.split('_')
    return int(hour)

def getDataFromFileName(fileName):
    (name, data, hour) = fileName.split(':')
    return int(date)

def getTimeFromRow(row):
    return row[1]

def getDateFromRow(row):
    return row[0]

def getHourFromRow(row):
    row[1]
    (h, m) = row[1].split(':')
    return int(h)

def getIdFromRow(row):
    return row[2]

def getModelFromRow(row):
    return row[3]

def getLatitudeFromRow(row):
    return float(row[4])

def getHeightFromRow(row):
    return float(row[8])

def getHeightWRFFromRow(row):
    return float(row[9])

def getRHFromRow(row):
    return float(row[11])

def getPressureFromRow(row):
    return float(row[12])

def getTemperatureFromRow(row):
    return float(row[10])

def calculeteG(height, heightWRF, latitude):
    try:
        g = 9.8063 * (1-(pow(10,-7) * ((heightWRF + height) / 2) * (1 - ((0.0026373 * math.cos(latitude * 2))) + (5.9 * pow(10,-6) * pow(math.cos(2 * latitude), 2) ))))
        return g
    except ArithmeticError:
        print("Gdzie jest szerokosc geodezyjna")

def calculeteP(temperature, height, pressure, heightWRF, latitude):
    try:
        g = calculeteG(height, heightWRF, latitude)
        fooValue = ((g * 0.0289644) / (0.0065 * 8.31432))

        p = pressure * pow(((temperature - (0.0065*(height - heightWRF))) / temperature), g)

        return p
    except ValueError:
        print("Something wrong in calculeteP")

def calculeteE(temperature, RH):
    try:
        Esat = calculeteEsat(temperature)
        E = (RH * Esat) / 100
        return E
    except ArithmeticError:
        print("Something wrong in calculeteE")

def calculeteEsat(temperature):
    try:
         valueFoo = math.exp((17.67 * (temperature - 273.15)) / ((temperature - 273.15) + 243.5))
         return 6.122 - valueFoo
    except ArithmeticError:
        print("Something wrong in calculeteEsat")

def readFromFile(fileName):
    try:
        with open(fileName) as file:
            dataFromFile = list(csv.reader(open(fileName)))
        return dataFromFile
    except FileNotFoundError:
        print("Couldnt find file")

def writeToFile(fileName, dataList):
    try:
        with open(fileName, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(dataList)
        csvfile.close()
    except FileExistsError:
        print("Something wrong in writeFile")

def calculeteZTDForRow(row):
    try:

        modelType = getModelFromRow(row)
        RH = getRHFromRow(row)
        temperature = getTemperatureFromRow(row)
        pressure = getPressureFromRow(row)
        height = getHeightFromRow(row)
        latitude = getLatitudeFromRow(row)
        heightWRF = getHeightWRFFromRow(row)

        if (modelType == "2m"):
            paraP = calculeteP(temperature, height ,pressure, heightWRF, latitude)
        else:
            paraP = getPressureFromRow(row)

        paraE = calculeteE(temperature, RH)
        ztd = 0.002277 * ( paraP +  (((1255/temperature) + 0.05)* paraE))
        return ztd
    except ValueError:
        print("Something wrong in calculeteZTDForRow")

def addInfoToListFromRow(row, helpList, filename):
    try:
        (file) = filename.split('\\')
        (namefile, extension) = file[2].split('.')
        (name, date, hour) = namefile.split('_')
        helpList.append(date)
        helpList.append(hour)
        helpList.append(getIdFromRow(row))
        helpList.append(getDateFromRow(row))
        helpList.append(getTimeFromRow(row))
        return helpList
    except ValueError:
        print("Cos sie zjebalo w addInfoToListFromRow")

def calculeteZTDForFile(data, filename):
    print(data)
    try:
        outZTD = []
        for row in data:
            helpList = []
            addInfoToListFromRow(row, helpList, filename)
            helpList.append(calculeteZTDForRow(row))
            outZTD.append(helpList)

        return outZTD
    except ArithmeticError:
        print("Something wrong in calculeteZTDFromFile")

def calculeteZTDForFilesInDirectiory(pathToDir):
    try:
        ZTDFromAllFiles = []
        for filename in glob.glob(os.path.join(pathToDir, '*.csv')):
            dataList = readFromFile(filename)
            ZTDFromAllFiles.append(calculeteZTDForFile(dataList, filename))


        return ZTDFromAllFiles
    except ValueError:
        print("Something went wrong in ZTDForFilesInDirectiory")

def calculateW(fileHour, hour):
    try:
        return (1 / (valueL + 2))
    except ValueError:
        print("Someting went wrong in calculateW")
def calculateAvgForHour(data):
    try:

        return outData
    except ValueError:
        print("Something went wrong in calculateAvgForHour")

pathToData = '.\Data'
listFoo = calculeteZTDForFilesInDirectiory(pathToData)
writeToFile("testout.csv", listFoo)
print (listFoo);
#data = readFromFile("test.csv")
#dataFoo = calculeteZTDForFile(data)
#writeToFile("Aaatest.csv", dataFoo)





