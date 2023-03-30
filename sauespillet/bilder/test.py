from sau import Sau

def test_sau():
    sau = Sau("sau", 50, 50)
    print(sau._posisjon_venstre(), sau._posisjon_topp())


test_sau()
