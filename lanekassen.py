# Målet med programmet er å finne ut hvor mye penger i fremtiden jeg har å rutte med 
# på når det kommer til å kjøpe bolig i forhold til lånet som må betales tilbake
# Og hvordan det er med å betale ned lånet.
# Hvor mye tjener jeg på å flytte til Vindern?
# Jeg trenger å vite hva er det jeg ca. trenger til en bolig
# Jeg har lyst til å ha mest penger å rutte med og minst mulig lån i fremtiden
# Finne ut om jeg flytter hvor mye må jeg spare for å åpnå målet (bolig)
# Ha så mye så mulig til bruk i hverdagen mens jeg sparer nødvendig
# Ha lite lån

ett_år = 166859
utbetalt_nå = 41715 #ikke stipend

resten = ett_år - utbetalt_nå #med stipend
stipend = 0.4

print("Utregninger")
print(f"Ett år: {ett_år}")
print(f"Utbetalt til nå: {utbetalt_nå}")
print(f"Resten: {resten}")
print(f"Stipend: {stipend}")
print()

etter_3år = ett_år * 2 + resten
stipend_etter_3år = stipend * float(etter_3år)
lån_etter_3år = etter_3år - stipend_etter_3år

print(f"Total etter 3år: {etter_3år}")
print(f"Stipend etter 3år: {stipend_etter_3år}")
print(f"Lån etter 3år: {lån_etter_3år}")
print()

stipend_etter_første_år = stipend * float(resten)
stipend_i_måneden_første_år = stipend_etter_første_år / 10
stipend_etter_vanlig_år = stipend * float(ett_år)
stipend_i_måneden_vanlig_år = stipend_etter_vanlig_år / 12
forskjell_med_og_uten_stipend_etter_3år = etter_3år - lån_etter_3år

print(f"Stipend etter første år: {stipend_etter_første_år}")
print(f"Stipend i måneden første år: {stipend_i_måneden_første_år}")
print(f"Stipend etter vanlig år: {stipend_etter_vanlig_år}")
print(f"Stipend i måneden vanlig år: {stipend_i_måneden_vanlig_år}")
print(f"forskjell_med_og_uten_stipend_etter_3år: {forskjell_med_og_uten_stipend_etter_3år}") #samme som stipend etter 3 år
print()
 
månedsleie_vindern_total =  7500 +       350 +   466
#totalleie               = leien + internett + annet
månedsleie_bislett = 5000

print(f"månedsleie_vindern_total: {månedsleie_vindern_total}")
print(f"månedsleie_bislett: {månedsleie_bislett}")

leie_ut_året_vindern = månedsleie_vindern_total * 10
leie_ett_år_vindern = månedsleie_vindern_total * 12
leie_ut_året_bislett = månedsleie_bislett * 10
leie_ett_år_bislett = månedsleie_bislett * 12
leie_3år_vindern = leie_ut_året_vindern + 2 * leie_ett_år_vindern
leie_3år_bislett = leie_ut_året_bislett + 2 * leie_ett_år_bislett

print(f"leie_ut_året_vindern: {leie_ut_året_vindern}")
print(f"leie_ett_år_vindern: {leie_ett_år_vindern}")
print(f"leie_ut_året_bislett: {leie_ut_året_bislett}")
print(f"leie_ett_år_bislett: {leie_ett_år_bislett}")
print(f"leie_3år_vindern: {leie_3år_vindern}")
print(f"leie_3år_bislett: {leie_3år_bislett}")
print()

#Stipendet betaler først, så kommer tallet jeg må betale selv
stipend_månedsleie_vindern_første_år = månedsleie_vindern_total - stipend_i_måneden_første_år
stipend_månedsleie_vindern_ett_år = månedsleie_vindern_total - stipend_i_måneden_vanlig_år
stipend_månedsleie_vindern_3år = (leie_3år_vindern - stipend_etter_3år) / 34

print(f"stipend_månedsleie_vindern_første_år: {stipend_månedsleie_vindern_første_år}")
print(f"stipend_månedsleie_vindern_ett_år: {stipend_månedsleie_vindern_ett_år}")
print(f"stipend_månedsleie_vindern_3år: {stipend_månedsleie_vindern_3år}")
print((stipend_månedsleie_vindern_første_år + stipend_månedsleie_vindern_ett_år*2)/3)

#print(f"den: {den}")