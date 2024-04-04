import gest_Cafeteria

#Test que comprueba que, el nombre, solo se componga de caractéres alfabéticos
def test_onlyAlpha():
    assert gest_Cafeteria.checkName("KawaFresa") == True #Todos los caractéres son alfabéticos, así que True
    assert gest_Cafeteria.checkName("Kawa Fresa") == True #El espacio es válido como parte del nombre, así que True
    assert gest_Cafeteria.checkName("K4w4Fr3s4") == False #Los números no son caractéres alfabéticos, así que False
    assert gest_Cafeteria.checkName("Kawa Fresa!") == False #El signo ! no es un caractér alfabético, así qeu False

#Test que comprueba que, el nombre, tenga un largo de entre 2 a 15 caractéres
def test_lenName():
    assert gest_Cafeteria.checkName("KawaFresa") == True #Tiene 9 caractéres, así que True
    assert gest_Cafeteria.checkName("K") == False #Tiene 1 caractér, así que False
    assert gest_Cafeteria.checkName("KawaFresaMuySabrosa") == False #Tiene 19 caractéres, así que False
    
#Test que comprueba que, los valores de tamaño de la lista, tengan valores enteros y sean de 1 a 48
def test_valSize():
    assert gest_Cafeteria.checkSizes("1, 2, 3") == True #Todos los valores son enteros, así que True
    assert gest_Cafeteria.checkSizes("a, 2, c") == True #Los valores no númericos son ignorados y hay un entero, así que True
    assert gest_Cafeteria.checkSizes("a, b, c") == False #Ni un valor es númerico, así que False
    assert gest_Cafeteria.checkSizes("1, 2, 3.3") == False #Hay un valor decimal, así que False
    assert gest_Cafeteria.checkSizes("1, 2, 49") == False #El 49 se sale del rango establecido, así que False
    assert gest_Cafeteria.checkSizes("-1, 0, 1, 2") == False #El -1 y 0 se salen del rango establecido, así que False

#Test que comprueba que, los valores de tamaño de la lista, esten en orden ascendente
def test_sizeOrder():
    assert gest_Cafeteria.checkSizes("1") == True #Un solo elemento es válido, así que True
    assert gest_Cafeteria.checkSizes("1, 2, 3") == True #Los elementos están en orden ascendente, así que True
    assert gest_Cafeteria.checkSizes("1, 3, 5") == True #Los elementos no tienen que ser consecutivos, así que True
    assert gest_Cafeteria.checkSizes("2, 3, 4, 1") == False #El 1 es menor al 4, así que False
    assert gest_Cafeteria.checkSizes("3, 2, 1") == False #Los elementos están en orden descendente, así que False
    
#Test que comprueba que, la lista de tamaños, posea entre 1 y 5 elementos
def test_sizeSize():
    assert gest_Cafeteria.checkSizes("1") == True #Un solo elemento es válido, así que True
    assert gest_Cafeteria.checkSizes("1, 2, 3, 4, 5") == True #5 elementos es válido, así que True
    assert gest_Cafeteria.checkSizes("1, 2, 3, 4, 5, 6") == False #6 elementos no es válido, así que False
    assert gest_Cafeteria.checkSizes("") == False #Un string vacío no es válido, así que False
    assert gest_Cafeteria.checkSizes(" ") == False #Un string con solo espacios en blanco no es válido, así que False

#Test que comprueba que, el formato de la entrada, tenga el formato correcto
def test_listFormat():
    assert gest_Cafeteria.checkFormat("KawaFresa, 1, 3, 5") == True #El nombre es la primera entrada y, después, está una lista 
                                                                    #de tamaños válidos, así que True
    assert gest_Cafeteria.checkFormat("KawaFresa, 1, 3, 5, , 6") == True #Los espacios en blanco son ignorados, así que True
    assert gest_Cafeteria.checkFormat("KawaFresa, 1, 3, 5,, 6") == True #2 comas seguidas son ignoradas, así que True
    assert gest_Cafeteria.checkFormat("1, 2, 3, 4, KawaFresa") == False #La lista de tamaños es la primera entrada y, después,
                                                                        #está el nombre, así que False
    assert gest_Cafeteria.checkFormat("1, KawaFresa, 2, 3, 4") == False #El nombre se encuentra en medio de la lista de tamaños,
                                                                        #así que False
    