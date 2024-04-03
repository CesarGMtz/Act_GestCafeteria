import gest_Cafeteria

# def test_increment():
#     assert gest_Cafeteria.increment(3) == 4

def test_onlyAlpha():
    assert gest_Cafeteria.checkName("KawaFresa") == True
    assert gest_Cafeteria.checkName("Kawa Fresa") == True
    assert gest_Cafeteria.checkName("K4w4Fr3s4") == False
