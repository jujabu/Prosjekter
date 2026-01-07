from .artikler import *

class Meny:
    
    def __init__(self, filnavn):
        self._pizzaer = []
        self._drikker = []
        self._sideretter = []
        self._desserter = []

        self._last_inn_fra_fil(filnavn)

    ##
    #Til nå bare testet med pizzaer
    def _last_inn_fra_fil(self, filnavn):
        with open(filnavn, "r", encoding="utf-8") as fil:
            
            for rad in fil:
                rad = rad.strip()

                kolonne = rad.split(";")
                pizza = Pizza(kolonne[0], kolonne[1])
                self._pizzaer.append(pizza)

    def skriv_ut(self):
        for pizza in self._pizzaer:
            print(pizza.hent_navn(), pizza.hent_pris())
    ##