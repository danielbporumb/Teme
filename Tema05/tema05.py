                    ##### Exercitii obligatorii #####

"""
1.Funcție care să calculeze și să returneze suma a două numere
"""

print("---------------------------------1------------------------------------")

def suma_doua_numere(a, b):
    suma = a + b
    return suma


a = int(input("Introduceti valoarea lui a = "))
b = int(input("Introduceti valoarea lui b = "))
print(f"Suma celor doua numere (a si b) este : {suma_doua_numere(a,b)}")

"""
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
"""

print("---------------------------------2------------------------------------")

def par_impar(numar):
    if numar % 2 == 0:
        return True
    else:
        return False


numar = int(input("Introduceti un nr. pt. a afla daca este par sau impar : "))
print(f"Numarul '{numar}' este par : {par_impar(numar)}")

"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""

print("---------------------------------3------------------------------------")

def caractere_nume(nume, prenume, prenume_secundar):
    nume_complet = nume + prenume + prenume_secundar # facem concatenare de string-uri
    return len(nume_complet)


nume = input("Introdu numele tau : ")
prenume = input("Introdu prenumele tau : ")
prenume_secundar = input("Introdu al doilea prenume : ")
print(f"Numele tau, '{nume} {prenume} {prenume_secundar}', are {caractere_nume(nume,prenume,prenume_secundar)} caractere.")

"""
4. Funcție care returnează aria dreptunghiului
"""

print("---------------------------------4------------------------------------")

def aria_dreptunghi(L, l):
    aria = L * l
    return aria


L = int(input("Introduceti lungimea dreptunghiului : "))
l = int(input("Introduceti latimea dreptunghiului : "))
print(f"Aria dreptunghiului este = {aria_dreptunghi(L,l)}")

"""
5. Funcție care returnează aria cercului
"""

print("---------------------------------5------------------------------------")

# import math
def aria_cerc(R):
    pi = 3.14159
    aria = pi * R**2
    # sau puteam sa importam libraria 'math' (import math) si sa folosim numarul 'pi' :
    # aria = math.pi * R**2
    return aria


R = int(input("Introduceti raza cercului : "))
print(f"Aria cercului este = {aria_cerc(R)}")

"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și False dacă nu găsește.
"""

print("---------------------------------6------------------------------------")

def gaseste(string_dat, caracter_x):
    return caracter_x in string_dat # returneaza direct True sau False


string_dat = input("Introduceti un cuvant/propozitie : ")
caracter_x = input("Introduceti caracterul de cautat : ")
print(f"Caracterul introdus se gaseste in string-ul introdus : {gaseste(string_dat,caracter_x)}")

"""
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
"""

print("---------------------------------7------------------------------------")

def lower_upper_case(text):
    x = 0
    y = 0
    for i in range(len(text)):
        if text[i].islower():
            x += 1
        elif text[i].isupper():
            y += 1
        else: # am pus si else: continue ca sa nu numere spatiile sau oricare alte caractere
            continue
    print(f"Nr. de caractere lower case este : {x}")
    print(f"Nr. de caractere upper case este : {y}")


text = input("Introduceti un cuvant/propozitie : ")
lower_upper_case(text)

"""
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
"""

print("---------------------------------8------------------------------------")

def numere_pozitive(lista):
    numere_poz = list()
    for nr in lista:
        if nr > 0:
            numere_poz.append(nr)
    return numere_poz


lista = [-1, 2, 3, -4, -6, 5, 6, 8]
print(f"Lista cu numere pozitive : {numere_pozitive(lista)}")

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
"""

print("---------------------------------9------------------------------------")

def fara_return(nr1, nr2):
    if nr1 > nr2:
        print(f"Primul nr '{nr1}' este mai mare decat al doilea nr '{nr2}'")
    elif nr2 > nr1:
        print(f"Al doilea nr '{nr2}' este mai mare decat primul nr '{nr1}'")
    else:
        print("Numerele sunt egale")


nr1 = int(input("Introduceti primul numar : "))
nr2 = int(input("Introduceti al doilea numar : "))
fara_return(nr1,nr2)

"""
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
"""

print("---------------------------------10-----------------------------------")

def numar_set(nr, set_nr):
    if nr not in set_nr:
        set_nr.add(nr)
        print(f"Am adaugat numarul nou in set")
        print(f"Setul este: {set_nr}")
        return True
    else:
        print(f"Nu am adaugat numarul in set. Acesta exista deja")
        return False


set_nr = {1, 3, 2, 5, 6, 7, 9, 10, 14, 22, 55, 56}
nr = int(input("Introduceti un numar de adaugat in set : "))
numar_set(nr, set_nr)
# nu imi returneaza True sau False, nu inteleg de ce

