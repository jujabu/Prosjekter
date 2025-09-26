#Tenker å lage et enkelt program som printer ut en meny som brukeren selv har valgt og sier hvor mye det koster totalt

#Pizzaer    pizza:pris
margherita = {
    "name" : "Margherita",
    "price" : 135
}
            
pepperoni = {
    "name" : "Pepperoni",
    "price" : 155
}
capricciosa = {
    "name" : "Capricciosa",
    "price" : 205
}

pizzaer = {
    "margherita":margherita,
    "pepperoni":pepperoni,
    "capricciosa":capricciosa
}

#Drikker    drikke:pris
cola = {
    "name" : "Coca Cola",
    "price" : 35
}
fanta = {
    "name" : "Fanta Orange",
    "price" : 35
}
vann = {
    "name" : "Vann u/ kullsyre",
    "price" : 25
}
drikker = {
    "cola" : cola,
    "fanta" : fanta,
    "vann" : vann
}

#Meny
meny = {
    "pizza" : pizzaer,
    "drikke" : drikker
}

#Printer ut alle kategoriene og produktenes detaljer som selges
def printMeny():
    
    for kategori_navn, kategori  in meny.items():
    
        #"Kategoriens navn"
        print(kategori_navn)
    
        for vare in kategori.values():
    
            #"Varen prisen"
            for produkt_detalj in vare.values():
    
                print(f"{produkt_detalj} ", end="")
    
            print()
    
        print()

printMeny()

#Navnene på funksjonene/prosedyrene sier mye om hva de gjør

#Lager en tom handlekurv
def lagNyHandlekurv():
    handlekurv = []
    return handlekurv

#Printer ut alle varene i gitt handlekurv
def visHandlekurv(handlekurv):
    print("Handlekurv:")
    for vare in handlekurv:
        print(vare)
    print()
    

#Legger gitt varen i gitt handlekurv
#Returnerer handlekurven med varen
def leggIHandlekurv(vare, handlekurv):
    handlekurv.append(vare)
    return handlekurv

#Legger sammen prisen av alle varene i handlekurven
#Skriver ut totalen
def visTotal(handlekurv):
    total = 0

    for vare in handlekurv:

        if vare in meny["pizza"]:
            total += meny["pizza"][vare]["price"]

        elif vare in meny["drikke"]:
            total += meny["drikke"][vare]["price"]

    print("Total:", total, "\n")

#Brukeren får se alle kategorier fra menyen
#Skriv inn en kategori
#Returnerer valgt kategori
def menyValg():

    print("Kategorier:")
    for kategori in meny.keys():
        print(kategori)
    print()

    valg = input("Velg kategori: ")
    print()
    return valg


#Brukeren får se alle pizzaene fra menyen
#Skriv inn en pizza
#Returnerer valgt pizza
def pizzaValg():
    
    print("Dette er alle pizzaene:")
    for pizza in meny["pizza"].keys():
        print(pizza)
    print()

    valg = input("Velg pizza: " )
    print()
    return valg

#Brukeren får se alle drikkene fra menyen
#Skriv inn en drikke
#Returnerer valgt drikke
def drikkeValg():

    print("Dette er alle drikkene:")
    for drikke in meny["drikke"].keys():
        print(drikke)
    print()

    valg = input("Velg drikke: " )
    print()
    return valg

#Test-program
nyHandlekurv = lagNyHandlekurv()

def program(handlekurv):
    kategori = menyValg()
    
    if kategori == "pizza":
        vare = pizzaValg()
        
    elif kategori == "drikke":
        vare = drikkeValg()
    
    
    handlekurv = leggIHandlekurv(vare, handlekurv)
    visHandlekurv(handlekurv)
    visTotal(handlekurv)
    print()

    #Kjører igjen
    program(handlekurv)

#Kjører første gang
print("Kjører program()\n")
program(nyHandlekurv)