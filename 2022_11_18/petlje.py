#     x                    cilj
pozicija_automobila = 0
pozicija_cilja = 10

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

for ime in ["marko", "milos", "marija", "ana", "sofija"]:
    print("Hello", ime)

print("Prva sledeca linija...")

for broj in [1, 2, 3, 4, 5, 6, 7]:
    print("Ovo je broj:", broj)


for broj in range(5, 10, 2):
    print("Stampanje broja:", broj)

for broj in range(100, 0, -1):
    print("Prikaz", broj)

pozicija_automobila = 0
pozicija_cilja = 10

# 0, 1, 2 .... 10

for trenutna_pozicija in range(pozicija_cilja + 1):
    pozicija_automobila = trenutna_pozicija
    print(pozicija_automobila == pozicija_cilja)

pocetna_godina = 2010
zavrsna_godina = 2021

print("************************")
for godina in range(zavrsna_godina, pocetna_godina, -1):
    print(godina)

for zvezda in range(100):
    print("*", end="")

print()

print("1\t2\t3")
print("*******************")
                # 1, 2, 3, 4, 5

# zeljeni_broj = int(input("Unesite broj: "))

# for brojac in range(1, zeljeni_broj + 1):
#     print(brojac * 1, end="\t")
#     print(brojac * 2, end="\t")
#     print(brojac * 3)


for x in range(5):         
    for y in range(3):     
        print("Ovo je X:", x, "Ovo je Y:", y)


'''
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #

'''

# * * * * *


for x in range(6):
    print(x, end="")
    for y in range(6):
        print("*", end= " ")
    print()



#kad su x i y jednaki tada su *, u suprotnom #
#* # # # #
# * # # #
# # * # #
# # # * #

for x in range(6):
    for y in range(6):
        if x == y:
            print("*", end= " ")
        else:
            print("#", end = " ")
        # print("*" if x == y else "#", end=" ")
    print()


#simbol = "*" if x == y else "#"




# print("Ovo je kurs \"Python\"")
# print("Ovo je deljenje, delim brojeve: a\\\\t")

#####################
#                   #
#                   #
#                   #
#                   #
######################

for x in range(10):
    for y in range(10):
        if x == 0 or x == 9 or y == 0 or y == 9:
            print("#", end= " ")
        else:
            print(" ", end=" ")
    print()