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
        from .bong import Bong
        
        bong = Bong(self._navn, self._telefonnummer, self._tid, self._dato, self._bestilling)
        return bong