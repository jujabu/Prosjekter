#Enkelt eksempel for testing
class Pizza:
    
    def __init__(self, navn, pris):
        self._navn = navn
        self._pris = pris
        self._ingredienser = []

    def hent_navn(self):
        return self._navn
    
    def hent_pris(self):
        return self._pris
    
    #Tar inn en liste med ingredienser
    def legg_til_ingredieser(self, ingredienser):
        self._ingredienser = ingredienser

    #Kanskje legg til?
    # def oppdater_pris(self, ny_pris):
    #     self._pris = ny_pris


class Drikke:
    
    def __init__(self, navn, pris):
        self._navn = navn
        self._pris = pris

    def hent_navn(self):
        return self._navn
    
    def hent_pris(self):
        return self._pris
    

class Siderett:
    
    def __init__(self, navn, pris):
        self._navn = navn
        self._pris = pris

    def hent_navn(self):
        return self._navn
    
    def hent_pris(self):
        return self._pris
    

class Dessert:
    
    def __init__(self, navn, pris):
        self._navn = navn
        self._pris = pris

    def hent_navn(self):
        return self._navn
    
    def hent_pris(self):
        return self._pris