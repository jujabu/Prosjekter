class Kunde:

    def __init__(self, navn, telefonnummer):
        self._navn = navn
        self._telefonnummer = telefonnummer

    def hent_navn(self):
        return self._navn
    
    def hent_telefonnummer(self):
        return self._telefonnummer