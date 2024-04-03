import re

def checkName(na):
    if (1 < len(na) < 16):
        return all(char.isalpha() or char.isspace() for char in na)
    else:
        return(False)

def checkSizes(si):
    # li = [float(num) if '.' in num else int(num) for num in re.split(r"[0-9]+.*[0-9]+.*[0-9]+.*[0-9]+\.[0-9]+.*[0-9]+\.[0-9]+.*[0-9]+\.[0-9]+", si)]
    li = [num.strip() for num in si.split(",")]
    lis = []
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
