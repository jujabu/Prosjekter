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
            for linje in fil:
                self._pizzaer.append(linje.strip())

    def skriv_ut(self):
        for pizza in self._pizzaer:
            print(pizza)
    ##