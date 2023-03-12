                    ##### Exercitii obligatorii #####

"""
1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a. Afiseaz-o
b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza varianta actuala (inversata)
c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii inverseze ordinea 
(Nu trebuie sa o suprascrii în acest caz, deoarece metoda face asta automat) si apoi printeaza  varianta actuala a 
listei. Practic ai ajuns înapoi la varianta inițială
Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi 
intr-o listă nouă. Metoda gasita de tine face suprascrierea automat și permanentizeaza aceste modificări. 
Ambele variante își găsesc utilitatea în funcție de ce ne dorim in acel moment.
"""

print("---------------------------------1------------------------------------")

note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(f"Notele muzicale : {note_muzicale}")
note_muzicale = note_muzicale[::-1]
print(f"Notele muzicale invers : {note_muzicale}")
note_muzicale.reverse()
print(f"Note muzicale invers - metoda 2: {note_muzicale}")

"""
2. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
"""

print("---------------------------------2------------------------------------")

print(f"Nota 'do' apare in lista de {note_muzicale.count('do')} ori")

"""
3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.
"""

print("---------------------------------3------------------------------------")

lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
lista_1_2 = lista_1 + lista_2 # metoda prin care concatenam cele 2 liste; merge si in cazul in care listele contin string-uri
print(f"Listele unite prin prima metoda : {lista_1_2}")
lista_1.extend(lista_2) # metoda prin care adaugi undei liste elementele altei liste; nu trebuie memorata intr-o alta variabila
print(f"Listele unite prin a doua metoda : {lista_1}")

"""
4. Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista
folosind o functie si apoi afiseaza din nou lista
"""

print("---------------------------------4------------------------------------")

lista_1.sort()
print(f"Lista sortata crescator : {lista_1}")
lista_1.remove(0)
# lista_1.pop(0) se poate si cu functia pop() in care specificam index-ul; in cazul de fata, avand int in lista, la ambele functii va fi remove(0) respectiv pop(0)
print(f"Lista sfara numarul '0' : {lista_1}")

"""
5. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura urmatoarele:
- Lista este goala (IF)
- Lista nu este goala (ELSE)
"""

print("---------------------------------5------------------------------------")

if lista_1 == list(): # am vazut la curs ca asa s-ar defini o lista goala
    print("Lista este goala")
else:
    print("Lista nu este goala")

# if len(lista_1) == 0: # se mai poate si asa: daca lungimea listei este 0, atunci lista este goala
#     print("Lista este goala")
# else:
#     print("Lista nu este goala")

"""
6. Foloseste o functie care sa goleasca lista de la exercitiul 3
"""

print("---------------------------------6------------------------------------")

lista_1.clear()
print(f"Lista dupa golire : {lista_1}")

"""
7. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se
afiseze ca lista e goala
"""

print("---------------------------------7------------------------------------")

if lista_1 == list(): # am vazut la curs ca asa s-ar defini o lista goala
    print("Lista este goala")
else:
    print("Lista nu este goala")

"""
8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa
afisezi Elevii (cheile)
"""

print("---------------------------------8------------------------------------")

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(f"Elevii din 'dict1' : {dict1.keys()}") # apare: Elevii din 'dict1' : dict_keys(['Ana', 'Gigel', 'Dorel'])

"""
9. Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
Ex: ‘Ana a luat nota {x}’.
Doar nota o vei lua folosindu-te de cheie
"""

print("---------------------------------9------------------------------------")

print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat nota {dict1['Dorel']}")

"""
10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
- Modifica nota lui Dorel in 6
- Printeaza nota lui dupa modificare
"""

print("---------------------------------10-----------------------------------")

dict1['Dorel'] = 6
# dict1.update({"Dorel": 6}) se mai poate si cu functia update()
print(f"Nota lui Dorel dupa contestatie este : {dict1['Dorel']}")

"""
11. Imagineaza-ti ca Gigel se transfera din clasa.
- Cauta o functie care sa il stearga
Vine un coleg nou.
- Adaugati-l in lista pe Ionica, cu nota 9
- Printati dictionarul cu noii elevi
"""

print("---------------------------------11-----------------------------------")

dict1.pop("Gigel")
print(f"Gigel s-a transferat. Au ramas elevii : {dict1}")
dict1["Ionica"] = 9
print(f"A venit noul coleg. Elevii sunt : {dict1}")

"""
12. Ai urmatoarele seturi:
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
- Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
- Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
"""

print("---------------------------------12-----------------------------------")

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(f"Setul dupa adaugare ziua 'luni': {zile_sapt}")
# dat fiind faptul ca seturile contin doar valori unice, daca adaugam o valoare care deja exista, aceasta nu o sa
# apara de doua ori, dar nici nu o sa primim eroare

"""
13. Foloseste un if si verifica daca:
- Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
regasesc intre elementele din setul zile_sapt)
- Weekend nu este un subset al zilelor din sapt
Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
punct de mai sus va fi un boolean
"""

print("---------------------------------13-----------------------------------")

print("Weekend este un subset al zilelor din sapt:")
if weekend.issubset(zile_sapt):
    print(True)
else:
    print(False)

if weekend <= zile_sapt:
    print(True)
else:
    print(False)
# nu sunt sigur daca la asta te-ai referit cand ai zis de metoda cu operatorul de comparatie, insa am testat si am
# vazut ca functioneaza, atata timp cat elementele din weekend sunt mai mici sau egale cu cele din zile_sapt, returneaza True

"""
14. Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
sunt in weekend si invers)
"""

print("---------------------------------14-----------------------------------")

print(f"Elementele care sunt in 'zile_sapt' si nu sunt in 'weekend': {zile_sapt.difference(weekend)}")
print(f"Elementele care sunt in 'weekend' si nu sunt in 'zile_sapt': {weekend.difference(zile_sapt)}")
# am gasit pe net aceasta functie care iti afiseaza elementele care se afla intr-un set si nu se afla in celalalt set
# in cazul al doilea, nu exista elemente care sa fie in 'weekend' si sa nu fie in 'zile_sapt', deci setul este gol => set()

diferenta1 = zile_sapt - weekend # s-ar mai putea si in acest fel, practic scadem 'sambata' si 'duminica' din 'zile_sapt'
print(f"Elementele care sunt in 'zile_sapt' si nu sunt in 'weekend': {diferenta1}")
diferenta2 = weekend - zile_sapt
print(f"Elementele care sunt in 'weekend' si nu sunt in 'zile_sapt': {diferenta2}")

"""
15. Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
ambele seturi). Hint: Va puteti folosi de o functie
"""

print("---------------------------------15-----------------------------------")

intersectie = zile_sapt.intersection(weekend)
print(f"Elementele care exista in ambele seturi: {intersectie}")