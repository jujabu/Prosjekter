from tredje_utkast import *

bestilling = Bestilling()
pizza = Pizza("Margherita", 135)
drikke = Drikke("Cola", 35)
bestilling.legg_til_vare(pizza)
bestilling.legg_til_vare(drikke)
bestilling.skriv_ut()

bong = Bong("Jesper", 95010321, "01:48", "05/01", bestilling)
bong.skriv_ut()

print("Test order")
jesper = Kunde("Jesper", 95010321)
order = Order(jesper, bestilling)
bong2 = order.lag_bong()
bong2.skriv_ut()

meny = Meny("meny.txt")
meny.skriv_ut()