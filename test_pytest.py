import gest_Cafeteria

# def test_increment():
#     assert gest_Cafeteria.increment(3) == 4

def test_onlyAlpha():
    assert gest_Cafeteria.checkName("KawaFresa") == True
    assert gest_Cafeteria.checkName("Kawa Fresa") == True
    assert gest_Cafeteria.checkName("K4w4Fr3s4") == False

def test_lenName():
    assert gest_Cafeteria.checkName("KawaFresa") == True
    assert gest_Cafeteria.checkName("K") == False
    assert gest_Cafeteria.checkName("KawaFresaMuySabrosa") == False
    
def test_valSize():
    assert gest_Cafeteria.checkSizes("1, 2, 3") == True
    assert gest_Cafeteria.checkSizes("1, 2, 3.3") == False
    assert gest_Cafeteria.checkSizes("0, 1, 2, 49") == False
    assert gest_Cafeteria.checkSizes("-1, 0, 1, 2") == False

def test_sizeOrder():
    assert gest_Cafeteria.checkSizes("1") == True
    assert gest_Cafeteria.checkSizes("1, 2, 3") == True
    assert gest_Cafeteria.checkSizes("1, 2, 3, 4, 5") == True
    assert gest_Cafeteria.checkSizes("2, 3, 4, 1") == False
    assert gest_Cafeteria.checkSizes("3, 2, 1") == False
    
def test_sizeSize():
    assert gest_Cafeteria.checkSizes("1") == True
    assert gest_Cafeteria.checkSizes("1, 2, 3, 4, 5") == True
    assert gest_Cafeteria.checkSizes("1, 2, 3, 4, 5, 6") == False
    assert gest_Cafeteria.checkSizes("") == False
    assert gest_Cafeteria.checkSizes(" ") == False
    