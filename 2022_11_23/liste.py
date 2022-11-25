osoba = ["Sofija", 25, "plava", False]
                    #4
                    # 0 1 2 3 4
for indeks in range(len(osoba)):
    print(osoba[indeks])

                # "Sofija", 25, "plava", False
for osobina in osoba:
    print(osobina)
                # 0 
voce_i_povrce = ["jabuka", "beli luk", "crni luk", "banana", "mandarina", "lubenica", "krastavac"]
# 0 jabuka
# 1 beli luk
# 2 crni luk
# 3 banana

for stavka in voce_i_povrce:
    print(stavka)
    print("Na indeksu ??? nalazi se...", stavka)

        # 0 7
for i in range(len(voce_i_povrce)):
    print("Na indeksu:", i, "nalazi se", voce_i_povrce[i])

for indeks, vrednost in enumerate(voce_i_povrce):
    print("Indeks:", indeks, "Stavka:", vrednost)
                #0        1      2
automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Opel", "Opel"]

# Pozicija: 0 Auto: Citroen
for pozicija, auto in enumerate(automobili):
    if len(auto) == 3:
        print(auto)
    #print("Pozicija:", pozicija, "Auto:", auto)
# prosirenje ponude
automobili.append("Mercedes")
automobili[2] = "Opel Corsa"
print(automobili)
automobili[3] = "Kia Sportage"

del automobili[3]
print(automobili)
automobili.remove("BMW")
print(automobili)
automobili.pop(0)
print(automobili)
                # 0 1 2 3 4 5 
automobili[0]
broj_opela = 0
for indeks in range(len(automobili)):
    if automobili[indeks] == "Opel":
        print("Evo ga opel")
        broj_opela += 1

print("Imam ", broj_opela, "na placu.")


automobili.clear()
print(automobili)

prazan_plac = []
#               0          1     2       3         4   5       6
automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Peugeot", "Audi"]

automobili_akcija = []

for i in range(len(automobili)):
    if i == 1 or i == 2 or i == 3:
        automobili_akcija.append(automobili[i])

print(automobili_akcija)

automobili_akcija = automobili[1:4:2]
print(automobili_akcija)

#lista
# prazne liste, parni neparni
# for
# %
# if else
brojevi = [1, 10, 12, 7, 3, 4, 2, 5]
parni = []
neparni = []

for broj in brojevi:
    parni.append(broj) if broj % 2 == 0 else neparni.append(broj)
    # if broj % 2 == 0:
    #     parni.append(broj)
    # else:
    #     neparni.append(broj)

print(parni, neparni)