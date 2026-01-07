from Klasser import *

handlekurv = Handlekurv()
pizza = Pizza("Margherita", 135)
drikke = Drikke("Cola", 35)
handlekurv.legg_til_artikkel(pizza)
handlekurv.legg_til_artikkel(drikke)
handlekurv.skriv_ut()

bong = Bong("Jesper", 95010321, "01:48", "05/01", handlekurv)
bong.skriv_ut()
print()

print("Test order:")
jesper = Kunde("Jesper", 95010321)
order = Order(jesper, handlekurv)
bong2 = order.lag_bong()
bong2.skriv_ut()

print()
meny = Meny("C:\Documents (not OneDrive)\Prosjekter\Kassesystem\Tredje_utkast\.tekstfiler\meny.csv")
meny.skriv_ut()