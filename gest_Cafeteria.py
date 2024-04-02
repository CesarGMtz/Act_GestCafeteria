import re

def checkName(na):
    if (1 < len(na) < 16):
        return all(char.isalpha() or char.isspace() for char in na)
    else:
        return(False)

def checkSizes(si):
    li = [int(num) for num in re.split("[^a-zA-Z\d]+",si)]
    for num in li:
        if (isinstance(num, int) and 0 < num < 49):
            print(num)
        else:
            return(False)
    return(True)

print("Agrega una nueva Bebida")
x = input()

name = x.split(",", 1)[0].strip()
sizes = x.split(",", 1)[1].strip()
print("Nombre: ")
print(checkName(name))
print("Tamaño: ")
print(checkSizes(sizes))
