import random

def getRandomNames(names, numNames):
    nameList = names
    random.shuffle(nameList)
    return nameList[0:numNames]