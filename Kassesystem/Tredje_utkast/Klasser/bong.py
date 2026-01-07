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