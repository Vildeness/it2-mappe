from sau import Sau

class Spillbrett:
    def __init__(self):
        self._sauer= []


    def opprett_sau(self, bilde, posisjon_venstre, posisjon_topp):
        sau = Sau(bilde, posisjon_venstre, posisjon_topp)
        if sau not in self._sauer:
            self._sauer.append(sau)

    def opptater(self):
        for sau in self._sauer:
            sau._beveg(self)

    def tegn(self, skjerm):
        for sau in self._sauer:
            sau.tegn(skjerm)