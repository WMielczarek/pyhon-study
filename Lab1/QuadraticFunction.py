from math import sqrt
def fuctionToCountDelta(paraA, paraB, paraC):
     delta = (paraB*paraB) - (4*paraA*paraC)
     return delta


def rootFuctionForDeltaEqualsZero(paraA, paraB):
    root = -paraB / 2 * paraA
    return root

def firstRoot(paraA, paraB, delta):
    firstRoot = (-paraB - sqrt(delta)) / 2 * paraA
    return firstRoot

def secondRoot(paraA, paraB, delta):
    secondRoot = (-paraB + sqrt(delta)) / 2 * paraA
    return secondRoot

def rootFuctionForDeltaBiggerThanZero(paraA, paraB, delta):
    try:
        firstRootA = firstRoot(float(paraA), float(paraB), float(delta))
        secondRootA = secondRoot(float(paraA), float(paraB), float(delta))
        return firstRootA, secondRootA
    except ValueError:
        print("Delta mniejsza niz zero")


print("Obliczam pierwiastki fukcji kwadratowej")
paraA = input("Podaj wartosc parametru A: ")
paraB = input("Podaj wartosc parametru B: ")
paraC = input("Podaj wartosc parametru C: ")

delta = fuctionToCountDelta(int(paraA), int(paraB), int(paraC))
print("Delta twojej fukcji wynosi: " + str(delta))

if delta == 0:
    print("b")
    print("Fukcja posiada tylko jedno miejsce zerowe: " + srt(rootFuctionForDeltaEqualsZero(int(paraA), int(paraB))))
else:
    firstRoot, secondRoot = rootFuctionForDeltaBiggerThanZero(int(paraA), int(paraB), int(delta))
    print("Fukcja posiada dwa miejsca zerowe: " + str(firstRoot) + " oraz " + str(secondRoot))

