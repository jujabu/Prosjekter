class Transaksjon:

    def __init__(self, dato, pris, tittel):
        self._dato = dato
        self._pris = pris
        self._tittel = tittel
        self._kvittering = ""

    def __str__(self):
        #Formatert tekst til utskrift
        # return "{:10.10} | {:>10.10} | {:28.28} | {}".format(self._dato, self._pris, self._tittel, self._kvittering)
        return "{};{};{};{}".format(self._dato, self._pris, self._tittel, self._kvittering)

    def har_kvittering(self):
        if self._kvittering:
            return True
        return False

    def oppdater_kvittering(self, lenke):
        self._kvittering = lenke