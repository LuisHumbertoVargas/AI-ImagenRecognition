print("Artemis Rover Rock Scanner Starting")

basalt = 0
breccia = 0
highland = 0
regolith = 0
rockList = []

strPath = "../FirstStage/rocks.txt"

fileObject = open(strPath)

line = fileObject.readline()
# Imprime un dato de tipo string
# print(type(line))
print(line)

print("================================")

rockList = fileObject.readlines()
# Imprime un dato de tipo lista
# print(type(rockList))
for rock in rockList:
    print(rock)

fileObject.close()

print("==========================")

def countMoonRocks(rockToID):
    global basalt
    global breccia
    global highland
    global regolith

    rockToID = rockToID.lower()

    if("basalt" in rockToID):
        print("Found a basalt\n")
        basalt += 1
    elif("breccia" in rockToID):
        print("Found a breccia\n")
        breccia += 1
    elif("highland" in rockToID):
        print("Found a highland\n")
        highland += 1
    elif("regolith" in rockToID):
        print("Found a regolith\n")
        regolith += 1

    return

# fileObject = open("rocks.txt")
# rockList = fileObject.readlines()

for rock in rockList:
    countMoonRocks(rock)

# TODO Add a print statement for the other types of rocks: breccia, highland and regolith
print("Number of Basalt: ", basalt)
print("Number of Basalt: ", breccia)
print("Number of Basalt: ", highland)
print("Number of Basalt: ", regolith)

# TODO Add other rock types to the "max" and "min" function calls
print("The max number of one type of rock found was:", max(basalt, breccia, highland, regolith ))
print("The minimum number of one type of rock found was:", min(basalt, breccia, highland, regolith))