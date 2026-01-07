class Kassesystem:
    
    def __init__(self):
        self._produksjonstid = 15

        self._utsolgte_artikler = [] #eller utsolgte_råvarer

class Handlekurv:
    
    def __init__(self):
        self._artikler =[]

    def legg_til_artikkel(self, artikkel):
        self._artikler.append(artikkel)

    def skriv_ut(self):
        for artikkel in self._artikler:
            print(f"{artikkel.hent_navn()}: {artikkel.hent_pris()}kr")


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

class Bestilling:
    
    def __init__(self, handlekurv):
        self._handlekurv = handlekurv


class Bong:
    
    def __init__(self, navn, telefonnummer, tid, dato, bestilling):
        self._navn = navn
        self._telefonnummer = telefonnummer
        self._tid = tid
        self._dato = dato
        self._bestilling = bestilling

    def skriv_ut(self):
        print(f"{self._navn}\n"
              + f"{self._telefonnummer}\n"
              + f"{self._tid}\n"
              + f"{self._dato}")
        self._bestilling.skriv_ut()


class Kunde:

    def __init__(self, navn, telefonnummer):
        self._navn = navn
        self._telefonnummer = telefonnummer

    def hent_navn(self):
        return self._navn
    
    def hent_telefonnummer(self):
        return self._telefonnummer
    

class Order:
    
    def __init__(self, kunde, bestilling):
        self._navn = kunde.hent_navn()
        self._telefonnummer = kunde.hent_telefonnummer()
        
        #Gjør det mulig å få klokkeslett og dato på tidspunktet orderen kommer
        import datetime
        tidspunkt = datetime.datetime.now()
        self._tid = tidspunkt.strftime("%H:%M")
        self._dato = tidspunkt.strftime("%d/%m")

        self._bestilling = bestilling

        #Skal være klar innen så så mange minutter...

    def lag_bong(self):
        bong = Bong(self._navn, self._telefonnummer, self._tid, self._dato, self._bestilling)
        return bong


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