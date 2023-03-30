class Sau:
    def _init__(self, sau, venstre, topp):
        self._sau = "bilder/{bilde}.png"
        self._posisjon_venstre = venstre
        self._posisjon_topp = topp
        self._fart_venstre = 1
        self._fart_topp = 1

    def sett_posisjon(self, venstre, topp):
        self._posisjon_venstre = venstre
        self._posisjon_topp = topp

    def hent_posisjon_venstre(self):
        return self._posisjon_venstre

    def hent_posisjon_topp(self):
        return self._posisjon_topp

    def hent_fart_venstre(self):
        return self._fart_venstre

    def hent_fart_topp(self):
        return self._fart_topp

    def sett_fart(self, ny_fart):
        self._fart_venstre = ny_fart
        self._fart_topp = ny_fart
        

    def beveg(self):
        self.posisjon_venstre = self._posisjon_venstre + self._fart_venstre
        self._posisjon_topp = self._posisjon_topp + self._fart_topp
    

    def snu(self):
        self._fart_venstre *= -1
        self._fart_topp *= -1

            

    def tegn(self, skjerm):
        pass

    


