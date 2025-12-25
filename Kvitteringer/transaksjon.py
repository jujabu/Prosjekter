class Transaksjon:

    def __init__(self, dato, pris, tittel, kvittering):
        self._dato = dato
        self._pris = pris
        self._tittel = tittel
        self._kvittering = kvittering

    def oppdater_kvittering(self, ny_kvittering):
        self._kvittering = ny_kvittering

    def skriv_ut(self):
        print(self._dato, self._pris, self._tittel, self._kvittering)