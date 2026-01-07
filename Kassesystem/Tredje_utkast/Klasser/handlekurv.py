class Handlekurv:
    
    def __init__(self):
        self._artikler =[]

    def legg_til_artikkel(self, artikkel):
        self._artikler.append(artikkel)

    def skriv_ut(self):
        for artikkel in self._artikler:
            print(f"{artikkel.hent_navn()}: {artikkel.hent_pris()}kr")