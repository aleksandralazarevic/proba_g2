osoba = ["Sofija", 25, True]
print(osoba[0])

# kljuc : vrednost, kljuc : vrednost, kljuc : vrednost

osoba_recnik = {"ime":"Sofija", "godine": 25, "plava": True}
print(osoba_recnik)
print(osoba_recnik["ime"])
print(osoba_recnik["godine"])

for i in osoba_recnik:
    print(osoba_recnik[i])

for (kljuc, vrednost) in osoba_recnik.items():
    print("Ovo je kljuc:", kljuc)
    print("Ovo je vrednost:", vrednost)

osoba2 = {}

osoba2["ime"] = "Marija"

print(osoba2)

osoba2["ime"] = "Sofija"
print(osoba2)

del osoba2["ime"]
print(osoba2)

poruke = {"en": "Hello", "sr": "Zdravo", "de": "Hallo"}
# ako je jezik en ILI sr ILI de -> prikazi
# u suprotnom prikazi gresku...

# jezik = input("Unesite jezik: ")

# if jezik == "en" or jezik == "sr" or jezik == "de":
#     print(poruke[jezik])
# else:
#     print("Nemamo ovaj prevod...")

poruke = {"en": "Hello", "sr": "Zdravo", "de": "Hallo"}

# ENGLESKI: Hello
# SRPSKI: Zdravo
# NEMACKI: Hallo

for (jezik, prevod) in poruke.items():
    if jezik == "en":
        print(f"ENGLESKI: {prevod}")
    elif jezik == "de":
        print(f"NEMACKI: {prevod}")
    else:
        print(f"SRPSKI: {prevod}")


selekcija = {
    "drzava": "Srbija", 
    "broj_pobeda": 0, 
    "boje_dresova": ["crvena", "bela"], 
    "brojevi_igraca": [9, 5, 13, 20]
    }

# Boja: bela
# Boja: crvena
for (kljuc, vrednost) in selekcija.items():
    # print("KLJUC:",kljuc)
    # print("VREDNOST:",vrednost)
    if kljuc == "boje_dresova":
        for boja in vrednost:
            print("Boja:", boja)
    elif kljuc == "brojevi_igraca":
        for broj in vrednost:
            print(f"Igrac broj: {broj}!!!")
    else:
        print(f"{kljuc}: {vrednost}")

# ime = "Sofija"
# godine = 25
# plava = True
# slobodna = False

# opis_devojke = f"Ime {ime} je {slobodna} i ima {godine} godina"

# print(opis_devojke)

#Marka: Citroen
#Model: C3
#Boja: crvena
#Boja: bela
#Boja: crna
#Nema alu felne :(
#Godiste: 2017
#Snaga motora je: 1.6
automobil = {
    "marka": "Citroen",
    "model": "C3",
    "boje": ["crvena", "bela", "crna"],
    "alu_felne": False,
    "godiste": 2017,
    "kubikaza": 1.6
}

for kljuc, vrednost in automobil.items():
    if kljuc == "marka":
        print(f"Marka automobila: {vrednost}")
    elif kljuc == "model":
        print(f"Model {vrednost}")
    elif kljuc == "boje":
        for boja in vrednost:
            print(f"Boja: {boja}")
    elif kljuc == "alu_felne":
        if vrednost:
            print("Ima alu felne")
        else: 
            print("Nema alu felne")
    elif kljuc == "godiste":
        print(f"Godiste: {vrednost}")
    elif kljuc == "kubikaza":
        print(f"Snaga motora: {vrednost}")


automobili = {
    "BG-123": {
        "marka": "Citroen",
        "model": "C3",
        "kubikaza": 1.6,
        "boje": ["crvena", "bela", "crna"]
    },
    "BG-451": {
        "marka": "Opel",
        "model": "Astra",
        "kubikaza": 2.0,
        "boje": ["plava", "metalik"]
    },
    "BG-789": {
        "marka": "Audi",
        "model": "Q2",
        "kubikaza": 2.0,
        "boje": ["srebrna", "metalik"]
    }
}

for reg, detalji in automobili.items():
    for kljuc, vrednost in detalji.items():
        print(f"{kljuc}: {vrednost}")
    print("----------------------------------")


kursevi = {
    "PPF" : {
        "naziv": "Python Fundamentals",
        "semestar": 1
    },
    "OOP" : {
        "naziv" : "Python Object Oriented",
        "semestar" : 1
    }
}

for id_kursa, detalji in kursevi.items():
    for k, v in detalji.items():
        print(k, v)


# LISTA []

# RECNIK { kljuc: vrednost }
# SKUP {}
boje_u_ponudi = {"bela", "plava", "crvena"}
print(boje_u_ponudi)

boje_u_ponudi.add("zuta")
boje_u_ponudi.remove("bela")
print(boje_u_ponudi)




