# Guardamos el nombre del archivo en una variable
strPath = "text.txt"
# Obtenemos y guardamos el archivo en una variable
fileObject = open(strPath)
# Leemos la variable para ver que nos devulve.
# En este caso es una lista de cadenas que guardamos en textList
textList = fileObject.readlines()
# Cerramos el archivo abierto
fileObject.close()
# Imprimimos el contenido de la lista de caracteres obtenidos
for line in textList:
    print(line)

print("===================")

firstLine = textList[1]
print(firstLine)

print("===================")

def OutputRocketText(days):
    rocketText = "We will launch in " + str(days) + " days"
    return print(rocketText)

OutputRocketText(5)
