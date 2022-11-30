# brojevi = [1, 2, 3, 5, 7, 8, 9]

# brojevi.sort()
# brojevi.reverse()

# print(brojevi)                 
    #    i-1 i
        # 0  1  2  3   4  5  6
brojevi = [9, 1, 3, 2, 5, 8, 7]
# od najmanjeg ka najvecem
#   9    1
# x    y
# privremeno 1
# while True:
#     izvrsena_zamena = False
#     for i in range(1, len(brojevi)):
#         if brojevi[i] < brojevi[i-1]:
#             privremena = brojevi[i] # 1
#             brojevi[i] = brojevi[i-1] # 9
#             brojevi[i-1] = privremena # 1
#             izvrsena_zamena = True
#     if izvrsena_zamena == False:
#         break
    
# print(brojevi)
      #         0         1      2
proizvodi = ["Telefon", "TV", "Laptop"]
cene      = [  100,      200,     300]

# proizvodi[0]   cene[0]
# proizvodi[1]   cene[1]
# proizvodi[2]   cene[2]
# 0, 1 ,2

#prebroj listu pr
for i in range(len(proizvodi)):
    print(proizvodi[i], cene[i]) 

     #        0          1   2       3         4         5                       
automobili = ["Audi", "BMW", "Yugo", "Citroen", "Kia", "Peugeot"]

# Automobil: ...
# 3
# ako je indeks 3 

for i in range(len(automobili)):
    if i == 3:
        print(automobili[i])
        print("Pogodak")


proizvodi = [   #   0             1             2
                ["iphone 11", "samsung s22", "xiaomi x3"],      # 0
                ["acer", "macbook", "dell"],                    # 1
                ["ipad", "samsung galaxy tab", "xiaomi tablet"] # 2
            ]
#proizvodi[0][1]  [i][j]
telefoni = ["iphone 11", "samsung s22", "xiaomi x3"]
laptopovi = ["acer", "macbook", "dell"]
tableti = ["ipad", "samsung galaxy tab", "xiaomi tablet"]

# for kategorija in proizvodi:
#     for stavka in kategorija:
#         print(stavka)

for i in range(len(proizvodi)):
    print(proizvodi[i])
    for j in range(len(proizvodi[i])):
        print(proizvodi[i][j])


hrana = [
            ["cokolada", "bombone", "palacinke"],
            ["sarma", "musaka", "kiseli kupus"],
            ["pecena paprika", "ajvar", "sopska"]
        ]

for kategorija in hrana:
    for jelo in kategorija:
        #print(jelo)
        if jelo == "sopska":
            print("Sopska nadjena!", jelo)
        #print("Naziv:", jelo)

      

ime = "Sofija"

poruka = f"Cao {ime} !!!"
print(poruka)

# a = 10
# b = 15

# sabiranje = f"Sabiranje brojeva {a} i {b} je {a+b}"

# print("Sabiranje brojeva", a, "i", b, "je", a+b)

# 
# biblioteka = [ 
#                 ["uvod u pajton", "nepoznat autor", 123],
#                  ["uvod racunare", "aleksandra lazarevic", 321]  
#              ]
#

biblioteka = [

]

while True:
    print("Odaberi komandu: 1-unos, 2-prikaz, 3-brisanje, > 3 izlaz")
    komanda = int(input("Unesite komandu: "))

    if komanda == 1:
        # unos knjige, preuzmi podatke
        naslov = input("Unesite naslov: ")
        autor = input("Unesite autora: ")
        isbn = int(input("Unesite isbn: "))
        biblioteka.append([naslov, autor, isbn])
        print("Dodata knjiga")
    if komanda == 2:
        for knjiga in biblioteka:
            for detalj in knjiga:
                print(detalj)
    if komanda == 3:
        #ovde vrsim brisanje
        kljucna_rec = input("Unesite naziv knjige koju zelite da obrisem. ")
        for knjiga in biblioteka:
            #proveravam detalje KNJIGE
            for detalj in knjiga:
                if detalj == kljucna_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana")
        if komanda > 3:
            break
    

