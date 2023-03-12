                ##### Exercitii obligatorii #####

"""
1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else

Folosim structura 'if else' in momentul in care trebuie sa executam linii de cod in functie de anumite conditii
Astfel, daca o conditie este respectata se executa o anumita secventa de cod iar in caz contrar, alta secventa de cod.

2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
daca este numar intreg mai mare ca 0)
"""

print("---------------------------------2------------------------------------")

x = int(input("Introduceti un numar: "))
if x > 0:
    print(f"Numarul '{x}' este numar natural")
else:
    print(f"Numarul '{x}' nu este numar natural")

"""
3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
"""

print("---------------------------------3------------------------------------")

if x < 0:
    print(f"Numarul '{x}' este numar negativ")
elif x == 0:
    print(f"Numarul '{x}' este numar neutru")
else:
    print(f"Numarul '{x}' este numar pozitiv")

"""
4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).
"""

print("---------------------------------4------------------------------------")

if -2 <= x <= 13: # if x >= -2 and x <= 13:
    print(f"Numarul '{x}' se afla in intervalul [-2:13]")
else:
    print(f"Numarul '{x}' nu se afla in intervalul [-2:13]")

# ar mai fi o modalitate utilizand functia range:
# if x in range(-2,14):
#     print(f"Numarul '{x}' se afla in intervalul [-2:13]")
# else:
#     print(f"Numarul '{x}' nu se afla in intervalul [-2:13]")


"""
5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia abs

Pentru a rezolva acest tip de exercitiu se face diferenta dintre numarul cel mai mare si numarul cel mai mic,
iar din rezultatul obtinut se mai scade 1 pentru a gasi cate numere sunt cuprinse intre doua numere.
"""

print("---------------------------------5------------------------------------")

x = int(input("x = "))
y = int(input("y = "))
if x == y:
    print(f"Numerele sunt egale. Nu exista diferenta intre ele.")
else:
    d = abs(x - y)
    # d = abs(d) - 1 # nu mai trebuie scazut 1 pt ca nu ne intereseaza sa excludem capetele de interval
    print(f"Diferenta dintre '{x}' si '{y}' este de {d} numere")
    if d < 5:
        print(f"Diferenta de numere dintre 'x' si 'y' este mai mica decat 5")
    else:
        print(f"Diferenta de numere dintre 'x' si 'y' nu este mai mica decat 5")

"""
6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
"""

print("---------------------------------6------------------------------------")

if not (x >= 5 and x <= 27):
    print(f"Numarul '{x}' nu se afla in intervalul [5:27]")
else:
    print(f"Numarul '{x}' se afla in intervalul [5:27]")

# ar mai fi o modalitate utilizand functia range:
# if x not in range(5,28):
#     print(f"Numarul '{x}' nu se afla in intervalul [5:27]")
# else:
#     print(f"Numarul '{x}' se afla in intervalul [5:27]")

"""
7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
daca nu, afiseaza care din ele este mai mare
"""

print("---------------------------------7------------------------------------")

y_nou = 5
if x == y_nou:
    print(f"Variabila 'x = {x}' si 'y = {y_nou}' sunt egale.")
elif x > y_nou:
    print(f"Variabilele nu sunt egale, iar 'x = {x}' este mai mare decat 'y = {y_nou}'.")
else:
    print(f"Variabilele nu sunt egale, iar 'y = {y_nou}' este mai mare decat 'x = {x}'.")

"""
8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
oarecare (nicio latura nu e egala).
"""

print("---------------------------------8------------------------------------")

latura_x = int(input("Latura x a triunghiului: "))
latura_y = int(input("Latura y a triunghiului: "))
latura_z = int(input("Latura z a triunghiului: "))

if latura_x == latura_y == latura_z:
    print("Triunghiul este echilateral")
elif (latura_x == latura_y) or (latura_x == latura_z) or (latura_y == latura_z):
    print("Triunghiul este isoscel")
else:
    print("Triunghiul este oarecare")

"""
9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
"""

print("---------------------------------9------------------------------------")
vocale = 'aeiouăî'
litera = input("Introduceti o litera: ")
if litera.lower() in vocale:
    print(f"Litera '{litera}' este vocala")
else:
    print(f"Litera '{litera}' este consoana")

# am pus conditia transformand litera introdusa in lowercase pentru ca indiferent daca introducem un uppercase,
# sa poata fi verificat in stringul 'vocale'

"""
10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
urmeaza:
a. Peste 9 => A
b. Peste 8 => B
c. Peste 7 => C
d. Peste 6 => D
e. Peste 4 => E
f. 4 sau sub => F
"""

print("---------------------------------10-----------------------------------")

nota_romania = float(input("Introduceti o nota: "))
if nota_romania > 0 and nota_romania <= 10:
    if nota_romania > 9:
        nota_america = 'A'
    elif nota_romania > 8:
        nota_america = 'B'
    elif nota_romania > 7:
        nota_america = 'C'
    elif nota_romania > 6:
        nota_america = 'D'
    elif nota_romania > 4:
        nota_america = 'E'
    # elif nota_romania <= 4:
    else:
        nota_america = 'F'
    print(f"Nota '{nota_romania}' din sistemul romanesc corespunde notei '{nota_america}' din sistemul american.")
else:
    print("Nota invalida. Introduceti o nota intre 1 si 10")

