                    ##### Exercitii bonus #####

"""
1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
inputuri urmatoarele informatii:
a. Varsta
b. Insotit de mama
c. Insotit de tata
d. Pasaport
e. Act permisiune mama
f. Act permisiune tata

Conditii de imbarcare:
1. Daca pers are varsta peste 18 ani si are pasaport
2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
si are permisiune in scris de la celalat parinte


Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.

Exemple:
1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
"""

print("---------------------------------1------------------------------------")

Varsta = int(input("Introduceti varsta: "))
Insotit_de_mama = input("Insotit de mama (da/nu): ") == "da"
Insotit_de_tata = input("Insotit de tata (da/nu): ") == "da"
Pasaport = input("Pasaport (da/nu): ") == "da"
Act_mama = input("Act permisiune mama (da/nu):  ") == "da"
Act_tata = input("Act permisiune tata (da/nu): ") == "da"
# am gasit pe net aceasta metoda prin care string-ul introdus cu functia 'input()' se converteste in boolean si
# verifica daca acesta este egal sau nu cu string-ul 'yes'
# daca este egal, string-ul va fi True, daca nu este egal, va fi False
# in felul acesta putem cumula (cu operatorii de comparare) aceste variabile de tip boolean in if-else
# am incercat si cu citirea de la tastatura a valorilor de tip boolean, insa nu a functionat cum ma asteptam

if Pasaport == True:
    if (Varsta >= 18):
        print(f"Varsta {Varsta} ani, am pasaport => Ma pot imbarca")
    elif (Varsta < 18):
        if (Insotit_de_mama == True) and (Insotit_de_tata == True):
            print(f"Varsta {Varsta} ani, am pasaport, ambii parinti => Ma pot imbarca")
        elif ((Insotit_de_tata == True) and (Act_mama == True)) or ((Insotit_de_mama == True) and (Act_tata == True)):
            print(f"Varsta {Varsta} ani, am pasaport, un parinte + act permisiune => Ma pot imbarca")
        else:
            print(f"Varsta {Varsta} ani, am pasaport, dar nu sunt insotit => Nu ma pot imbarca")
else:
    print(f"Varsta {Varsta} ani, nu am pasaport => nu ma pot imbarca")

# acelasi exercitiu, dar cu toata logica pusa intr-o functie

def imbarcare(varsta, insotit_de_mama, insotit_de_tata, pasaport, act_mama, act_tata):
    if (varsta >= 18) and pasaport:
        return True
    elif (varsta < 18) and pasaport and insotit_de_mama and insotit_de_tata:
        return True
    elif (varsta < 18) and pasaport and ((insotit_de_mama and act_tata) or (insotit_de_tata and act_mama)):
        return True
    else:
        return False

# Scenarii de testare:

# Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
assert imbarcare(19, False, False, False, False, False) == False
print("Varsta 19 ani, nu am pasaport => Nu ma pot imbarca")

# Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
assert imbarcare(17, True, True, True, False, False) == True
print("Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca")

# Varsta 20 ani, am pasaport => Ma pot imbarca
assert imbarcare(20, False, False, True, False, False) == True
print("Varsta 20 ani, am pasaport => Ma pot imbarca")

# Varsta 17 ani, nu am pasaport => Nu ma pot imbarca
assert imbarcare(17, False, False, False, False, False) == False
print("Varsta 17 ani, nu am pasaport => Nu ma pot imbarca")

# Varsta 17 ani, am pasaport, insotit de mama si act de la tata => Ma pot imbarca
assert imbarcare(17, True, False, True, False, True) == True
print("Varsta 17 ani, am pasaport, insotit de mama si act de la tata => Ma pot imbarca")

# Varsta 17 ani, am pasaport, insotit de tata si act de la mama => Ma pot imbarca
assert imbarcare(17, False, True, True, True, False) == True
print("Varsta 17 ani, am pasaport, insotit de tata si act de la mama => Ma pot imbarca")

# Varsta 16 ani, am pasaport, nu sunt insotit => Nu ma pot imbarca
assert imbarcare(16, False, False, True, False, False) == False
print("Varsta 16 ani, am pasaport, nu sunt insotit => Nu ma pot imbarca")

# Varsta 15 ani, am pasaport, insotit de un parinte, fara act celalalt parinte => Nu ma pot imbarca
assert imbarcare(15, True, False, True, False, False) == False
print("Varsta 15 ani, am pasaport, insotit de mama, fara act celalalt parinte => Nu ma pot imbarca")

assert imbarcare(15, False, True, True, False, False) == False
print("Varsta 15 ani, am pasaport, insotit de tata, fara act celalalt parinte => Nu ma pot imbarca")

# Varsta 15 ani, nu am pasaport, insotit de ambii parinti => Nu ma pot imbarca
assert imbarcare(15, True, True, False, False, False) == False
print("Varsta 15 ani, nu am pasaport, insotit de ambii parinti => Nu ma pot imbarca")

# Varsta 15 ani, nu am pasaport, insotit de un parinte si act de la celalalt parinte => Nu ma pot imbarca
assert imbarcare(15, True, False, False, False, True) == False
print("Varsta 15 ani, nu am pasaport, insotit de mama si act de la tata => Nu ma pot imbarca")

assert imbarcare(15, False, True, False, True, False) == False
print("Varsta 15 ani, nu am pasaport, insotit de tata si act de la mama => Nu ma pot imbarca")

"""
2. Joc de noroc
- Cauta pe net si vezi cum se genereaza un numar random
- Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
Numarul salvat va fi generat random cu metoda gasita in online
- Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
- Verifica si afiseaza daca utilizatorul a ghicit numarul
- Vor exista 3 optiuni care vor trebui tratate:
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari? Ai ales x si zarul a fost y
"""

print("---------------------------------2------------------------------------")

import random

dice_roll = random.randint(1, 6) # functia random.randinit prin care se genereaza numere intregi in intervalul specificat
numar = int(input("Introdu un numar de la 1 la 6: "))
print(f"Ai ales numarul '{numar}'")
if (numar > 6) or (numar < 1):
    print("Numarul introdus nu se afla in intervalul [1:6]")
elif numar == dice_roll:
    print(f"Ai ghicit. Felicitari! Ai ales '{numar}' si zarul a fost '{dice_roll}'")
elif numar < dice_roll:
    print(f"Ai pierdut. Ai ales un numar mai mic. ai ales '{numar}' dar a fost '{dice_roll}'")
# elif numar > dice_roll: # nu mai e neaparat sa dai ultima conditie
else:
    print(f"Ai pierdut. Ai ales un numar mai mare. ai ales '{numar}' dar a fost '{dice_roll}'")