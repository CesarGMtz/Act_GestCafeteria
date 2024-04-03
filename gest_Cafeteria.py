import re

def checkName(na):
    if (1 < len(na) < 16):
        return all(char.isalpha() or char.isspace() for char in na)
    else:
        return(False)

def checkSizes(si):
    if (si.isspace() or si == ""):
        return(False)
    
    li = [num.strip() for num in si.split(",")]
    i = 1

    if (0 < len(li) < 6):
        while i < len(li):
            if (li[i] < li[i - 1]):
                return(False)
            i += 1
    else:
        return(False)

    for num in li:
        if ("." in num):
            return(False)
        else:
            tNum = int(num)
            if (isinstance(tNum, int) and 0 < tNum < 49):
                print(num)
            else:
                return(False)
    return(True)

# print("Agrega una nueva Bebida")
# x = input()

# name = x.split(",", 1)[0].strip()
# sizes = x.split(",", 1)[1].strip()
# print("Nombre: ")
# print(checkName(name))
# print("Tamaño: ")
# print(checkSizes(sizes))
