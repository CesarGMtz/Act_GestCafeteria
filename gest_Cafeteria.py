#Se importa las librerias a usar
import re

#Función que checa si el formato, de la bebida agregada, es correcto
def checkFormat(dr):
    #Obtiene el primer elemento del string de la bebida, presuntamente el nombre de esta
    name = dr.split(",", 1)[0].strip()
    #Obtiene el resto del string de la bebida, presuntamente la lista de tamaños de esta
    sizes = dr.split(",", 1)[1].strip()
    
    #Checa si el string de entrada, el nombre y la lista de tamaños tienen formato correcto
    if(checkName(name) and checkSizes(sizes)):
        return(True) #Si sí, devuelve True
    else:
        return(False) #Si no, False


#Función que checha si el formato, del nombre de la bebida agregada, es correcto
def checkName(na):
    #Checa si el string del nombre tiene entre 2 y 15 caracteres
    if (1 < len(na) < 16):
        return all(char.isalpha() or char.isspace() for char in na) #Si sí, devuelve True si todos los caracterés del nombre 
                                                                    #son una letra o un espacio, si no, False 
    else:
        return(False) #Si no, False


#Función que checa si el formato, de la lista de tamaños de la bebida agregada, es correcto
def checkSizes(si):
    #Checa si el string de la lista de tamaños es solamente espacios en blanco o si está vacía
    if (si.isspace() or si == ""):
        return(False) #Si sí, devuelve True
    
    #Se crea una lista que contiene todos los valores númericos del string
    li = re.findall(r'\d+\.\d+|\d+', si)
    
    i = 1 #Se declara un contador para el ciclo
    #Checa si la lista tiene entre 1 y 5 elementos
    if (0 < len(li) < 6):
        #Si sí, se crea un ciclo que se repetirá por cada elemento de la lista
        while i < len(li):
            #Checa si el elemento visto de la lista es menor al que le precede
            if (li[i] < li[i - 1]):
                return(False) #Si sí, devuelve False
            i += 1 #Si no, revisa el elemento siguiente
    else:
        return(False) #Si no, False

    #Se crea un ciclo que se repetirá por cada elemento de la lista
    for num in li:
        #Checa si "." se encuentra en el string del número
        if ("." in num):
            return(False) #Si sí, devuelve False
        else:
            #Si no, se tranforma el string del número a integer
            tNum = int(num)
            #Checa si el valor del tamaño se encuentra entre 1 y 48
            if (0 < tNum < 49):
                print(num) #Si sí, imprimimos el número
            else:
                return(False) #Si no, False
    return(True) #Si no, True


# print("Agrega una nueva Bebida")
# drink = input()

# if (checkFormat(drink)):
#     print('Bebida Agregada Exitosamente')
# else:
#     print('Proceso Fallido')
