                    ##### Exercitii optionale #####

"""
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
"""

print("---------------------------------1------------------------------------")

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f"Numere pare : {numere_pare}")
print(f"Numere impare : {numere_impare}")
print(f"Numere pozitive : {numere_pozitive}")
print(f"Numere negative : {numere_negative}")

"""
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
"""

print("---------------------------------2------------------------------------")

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
    for j in range(0, len(alte_numere)- i - 1):
        if alte_numere[j] > alte_numere[j+1]: # daca nr curent > decat urmatorul
            alte_numere[j], alte_numere[j+1] = alte_numere[j+1], alte_numere[j] # se schimba intre ele
print(f"Lista sortata: {alte_numere}")

"""
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
"""

print("---------------------------------3------------------------------------")

import random
numar_secret = random.randint(1, 30)
Numar_ghicit = None
while Numar_ghicit != numar_secret: # cat timp numarul ghicit e diferit de numarul secret, executa bucla
    Numar_ghicit = int(input("Introdu un numar intre 1 si 30 : "))
    if (Numar_ghicit < 1) or (Numar_ghicit > 30):
        print("Numarul nu se afla in intervalul 1 - 30")
    elif Numar_ghicit == numar_secret:
        print("Felicitari! Ai ghicit!")
    elif Numar_ghicit < numar_secret:
        print("Nr. secret e mai mare.")
    else:
        print("Nr. secret e mai mic.")

"""
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777
Ex:3
1
22
333
"""

print("---------------------------------4------------------------------------")

dimensiune = int(input("Introdu dimensiunea piramidei : "))
# print(range(1, dimensiune+1))
for n in range(1, dimensiune+1): # ii specificam sa inceapa de la 1, altfel incepe de la 0
    for m in range(1, n+1, 1):
        print(n, end="")
    print()

"""
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
"""

print("---------------------------------5------------------------------------")

tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]

for t1 in range(len(tastatura_telefon)):
    for t2 in range(len(tastatura_telefon[t1])):
        print(f"Cifra curenta este '{tastatura_telefon[t1][t2]}'")