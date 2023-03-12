                    ##### Exercitii optionale #####

"""
1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
"""

print("---------------------------------1------------------------------------")

x1 = int(input("Introduceti un numar: ")) # puteam sa citim fara typecasting, deoarece valoarea citita era default un string
numar = str(abs(x1)) # transformam valoarea absoluta a numarul introdus intr-un string pentru a-i putea calcula lungimea
if len(numar) >= 4:
    print(f"Numarul 'x={x1}' are minim 4 cifre")
else:
    print(f"Numarul 'x={x1}' nu are minim 4 cifre")

"""
2. Verifica daca x are exact 6 cifre
"""

print("---------------------------------2------------------------------------")

x2 = int(input("Introduceti un numar: "))
numar2 = str(abs(x2))
if len(numar2) == 6:
    print(f"Numarul 'x={x2}' are exact 6 cifre")
else:
    print(f"Numarul 'x={x2}' nu are exact 6 cifre")

"""
3. Verifica daca x este numar par sau impar
"""

print("---------------------------------3------------------------------------")

x3 = int(input("Introduceti un numar: "))
if x3 % 2 == 0:
    print(f"Numarul 'x={x3}' este par")
else:
    print(f"Numarul 'x={x3}' este impar")

"""
4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre ele
"""

print("---------------------------------4------------------------------------")

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
if (x > y) and (x > z):
    print(f"Numarul 'x={x}' este cel mai mare")
elif (y > x) and (y > z):
    print(f"Numarul 'y={y}' este cel mai mare")
elif (z > x) and (z > y):
    print(f"Numarul 'z={z}' este cel mai mare")
elif x == y == z:
    print("Cele trei numere sunt egale")
else:
    print("Doua din numere sunt egale si sunt mai mari decat al treilea")

"""
5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
lungimea celei de-a treia laturi)
"""

print("---------------------------------5------------------------------------")

unghi_x = int(input("Introduceti primul unghi al triunghiului: "))
unghi_y = int(input("Introduceti al doilea unghi al triunghiului: "))
unghi_z = int(input("Introduceti al treilea unghi al triunghiului: "))
# latura_x = int(input("Introduceti lungimea primei laturi a triunghiului: "))
# latura_y = int(input("Introduceti lungimea celei de-a doua latura a triunghiului: "))
# latura_z = int(input("Introduceti lungimea celei de-a treia latura a triunghiului: "))
suma_unghiuri = x + y + z
if (suma_unghiuri == 180): #or (latura_x + latura_y > latura_z) or (latura_x + latura_z > latura_y) or (latura_y + latura_z > latura_x):
    print("Triunghiul este valid")
else:
    print("Triunghiul nu este valid")

"""
6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
smarte'
"""

print("---------------------------------6------------------------------------")

text = "Coral is either the stupidest animal or the smartest rock"
x_t = int(input("Nr. de caractere de sters: "))
print(f"Textul fara ultimele {x_t} caractere este: \n {text[:len(text) - x_t]}") # printam textul de la inceput pana la lungime - nr. introdus

"""
7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
din primele 5 caractere + ultimele 5
"""

print("---------------------------------7------------------------------------")

text_nou = text[:5] + text[-5:] # citim textul de la inceput pana la pozitia 5, respectiv ultimele 5 caractere si le concatenam
print(f"Primele 5 + ultimele 5 caractere: \n {text_nou}")

"""
8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
(hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
animal or the smartest '
"""

print("---------------------------------8------------------------------------")

cuvantul_rock = text.find('rock')
print(f"Cuvantul 'rock' incepe de la pozitia '{cuvantul_rock}'") # de la pozitia 53 incepe cuvantul 'rock'
text_taiat = text[:cuvantul_rock] # luam textul de la inceput, pana la pozitia 53
print(f"Textul taiat: \n {text_taiat}")

"""
9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
functie pentru a face string-ul case insensitive)
"""

print("---------------------------------9------------------------------------")

def case_insensitive(caracter1,caracter2):
    # return caracter1.lower() == caracter2.lower() # functia transforma din majuscule si verifica daca sunt egale
    return caracter1.casefold() == caracter2.casefold() # functia transforma din majuscule si verifica daca sunt egale - more recommanded
cuvant = input("Introduceti un text: ")
#print(f"Prima si ultima litera sunt egale: {case_insensitive(cuvant[:1],cuvant[-1:])}") # accesam in functie prima si ultima litera din string

assert case_insensitive(cuvant[:1],cuvant[-1:]), "Prima si ultima litera nu sunt egale"
print("Prima si ultima litera sunt egale")

"""
10. Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
(hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)
"""

print("---------------------------------10-----------------------------------")

sir = "0123456789"
print(f"Numerele pare din string: {sir[0:len(sir):2]}")
print(f"Numerele impare din string: {sir[1:len(sir):2]}")

# avand un string predefinit cu numere de la 0 la 9, pentru numere pare afisam string-ul de la 0 la final din 2 in 2
# iar pentru cele impare, afisam string-ul de la 1 la final, tot din 2 in 2