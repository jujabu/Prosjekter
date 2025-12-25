from transaksjon import Transaksjon

class Konto:

    def __init__(self):
        self._transaksjoner = []
        self._last_inn_fra_fil()

    def _last_inn_fra_fil(self):

        csv_fil = "brukskonto" + ".csv"

        with open(csv_fil, "r") as fil:

            for rad in fil:
                kolonne = rad.split(";")
                
                                        #(dato,       pris,       tittel,     kvittering)
                transaksjon = Transaksjon(kolonne[0], kolonne[1], kolonne[5], "")
                self._transaksjoner.append(transaksjon)


    def skriv_ut_alle_transaksjoner(self):
        
        print("UTGIFTER:")
        for transaksjon in self._transaksjoner:
            transaksjon.skriv_ut()