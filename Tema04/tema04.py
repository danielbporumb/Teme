                    ##### Exercitii obligatorii #####

"""
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
"""

print("---------------------------------1------------------------------------")

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
print("Varianta cu for : ")
for m in range(len(masini)):
    print(f"Masina mea preferata este {masini[m]}")
    m += 1

print("\nVarianta cu for each : ")
for masina in masini:
    print(f"Masina mea preferata este {masina}")

print("\nVarianta cu while : ")
p = 0
while p < len(masini): # len(masini) ii defapt 9
    print(f"Masina mea preferata este {masini[p]}")
    p += 1

"""
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule, exceptând primul și ultimul.
În else:
- Printează lista.
"""

print("---------------------------------2------------------------------------")

for n in range(1, (len(masini)-1)): # pornim de la index 1 pana la index 7 pt a exclude primul si ultimul (len(masini)=9 dar ultima nu se ia in calcul deci ar fi 8, din care mai scadem 1)
    masini[n] = masini[n].upper() # elementele din range se iau rand pe rand si li se aplica functia .upper
    n += 1
else:
    print(f"Lista cu masini cu majuscule : \n {masini}")

"""
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
"""

print("---------------------------------3------------------------------------")

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina_dorita in masini:
    if masina_dorita == "Mercedes":
        print(f"Am gasit masina dorita de dvs.: {masina_dorita}")
        break
    else: # am pus else-ul indentat la if ca sa imi afiseze cautarile pana in momentul in care gaseste Mercedes
        print(f"Am gasit masina {masina_dorita}. Mai cautam")

"""
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
"""

print("---------------------------------4------------------------------------")

for masina_de_bogatan in masini:
    if masina_de_bogatan == "Trabant" or masina_de_bogatan == "Lăstun":
        # print(masina_de_bogatan)
        continue
    print(f"S-ar putea sa va placa masina {masina_de_bogatan}")

"""
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
"""

print("---------------------------------5------------------------------------")

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = list()

for vechitura in masini:
    if vechitura == "Lăstun":
        masini_vechi.append(vechitura) # daca e Lastun, o adaugam in lista goala
        # masini[masini.index("Lăstun")] = "Tesla" # am vazut ca se poate sa suprascri direct valoarea de la un index si asa
        masini.insert(masini.index("Lăstun"), "Tesla") # inseram pe index-ul ei "Tesla"
        masini.pop(masini.index('Lăstun'))  # scoatem Lastun pe baza de index
    if vechitura == "Trabant":
        masini_vechi.append(vechitura) # daca e Trabant, o adaugam in lista goala
        # masini[masini.index("Trabant")] = "Tesla" # am vazut ca se poate sa suprascri direct valoarea de la un index si asa
        masini.insert(masini.index("Trabant"), "Tesla")  # inseram pe index-ul lui "Tesla"
        masini.pop(masini.index('Trabant'))  # scoatem Trabant pe baza de index
print(f"Modele vechi : {masini_vechi}")
print(f"Modele noi : {masini}")

"""
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printeaza "Pentru un buget de sub 15k puteti alege masina x" iterand prin lista cheilor dictionarului 
● Iterează prin listă.
"""

print("---------------------------------6------------------------------------")

pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}

buget = 15000
print(pret_masini.items())
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f"Masinile care se incadreaza in bugetul dvs. sunt : {masina}")

for masina in pret_masini.keys():
    if pret_masini[masina] <= buget:
        print(f"Pentru un buget de sub {buget} de euro puteti alege masina : {masina}")

"""
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""

print("---------------------------------7------------------------------------")

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
aparitie = 0
for aparitie in numere:
    if aparitie == 3:
        aparitie += 1
print(f"Numarul '3' apare in lista de {aparitie} ori")

"""
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""

print("---------------------------------8------------------------------------")

suma = 0
for nr in numere:
    suma += nr
print(f"Suma numerelor din lista este : {suma}")

"""
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
"""

print("---------------------------------9------------------------------------")

cmmnr = numere[0] # presupunem ca cel mai mare numar este primul din lista (sau oricare altul)
for i in range(len(numere)): # accesam lista de la inceput pana la sfarsit
    if numere[i] > cmmnr: # daca oricare element este mai mare decat cmmnr, acesta ia valoarea cmmnr
        cmmnr = numere[i]
print(f"Cel mai mare numar din lista : {cmmnr}")

"""
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
"""

print("---------------------------------10-----------------------------------")

for j in range(len(numere)):
    if numere[j] > 0:
        numere[j] = -numere[j]
print(f"Numerele pozitive din lista inlocuite cu valoarea lor negativa sunt: \n {numere}")

                    ##### Exercitii optionale #####

# Exercitiile optionale o sa le incarc doar pe duminica..