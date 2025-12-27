from transaksjon import Transaksjon

class Konto:

    def __init__(self, filnavn):
        self._transaksjoner = []
        self._last_inn_fra_fil(filnavn)

    #Laster inn csv-fil fra banken og formaterer til min versjon
    def _last_inn_fra_fil(self, filnavn):

        with open(filnavn, "r") as fil:

            for rad in fil:
                kolonne = rad.split(";")
                
                #Formatering
                dato = " ".join(kolonne[0].split())
                pris = " ".join(kolonne[1].split())
                tittel = " ".join(kolonne[5].split())

                transaksjon = Transaksjon(dato, pris, tittel)
                self._transaksjoner.append(transaksjon)

    #Laster inn min versjon av csv-fil
    def _last_inn_min_fil(self):

        csv_fil = "filtrert_konto.csv"

        with open(csv_fil, "r") as fil:

            for rad in fil:
                kolonne = rad.split(";")
                
                #Formatering
                dato = kolonne[0]
                pris = kolonne[1]
                tittel = kolonne[5]

                transaksjon = Transaksjon(dato, pris, tittel)
                self._transaksjoner.append(transaksjon)





    def skriv_ut_alle_transaksjoner(self):
        
        print("UTGIFTER:")
        for transaksjon in self._transaksjoner:
            print(str(transaksjon))


    def lagre_alle_transaksjoner(self):
        
        csv_fil = "filtrert_konto.csv"

        with open(csv_fil, "w") as fil:

            for transaksjon in self._transaksjoner:
                
                #Ser om det er siste element sånn at den ikke lager ny linje på siste
                if self._transaksjoner.index(transaksjon) == len(self._transaksjoner) - 1:
                    fil.write(str(transaksjon))
                else:
                    fil.write(str(transaksjon) + "\n")