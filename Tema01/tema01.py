                ##### Exercitii obligatorii #####
"""
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

- o variabila este o zona de memorie care tine diferite date
"""

"""
# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă :
- string
- int
- float
- bool
Observație: Valorile vor fi alese de tine după preferințe.
"""
marca_masina = "Audi"
an_fabricatie = 2012
lungime = 4.7
inmatriculata = True

print("---------------------------------3------------------------------------")

"""
3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
"""

print(f"Variabila 'marca_masina' este de tipul: {type(marca_masina)}")
print(f"Variabila 'an_fabricatie' este de tipul: {type(an_fabricatie)}")
print(f"Variabila 'lungime' este de tipul: {type(lungime)}")
print(f"Variabila 'inmatriculata' este de tipul: {type(inmatriculata)}")

print("---------------------------------4------------------------------------")

"""
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
"""

lungime = round(lungime)
print(f"Lungimea masinii dupa rotunjire este de: {lungime} m")
print(f"Tipul variabilei 'lungime' dupa rotunijre este : {type(lungime)}")

print("---------------------------------5------------------------------------")

"""
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
"""

print("Detin o masina marca " + marca_masina) # print de 2 string-uri
print("Este fabricata in anul " + str(an_fabricatie)) # print de un string + un int, motiv pt care folosim type casting
print(f"Are ca si lungime aproape {lungime} m") # print de un string + un int, motiv pt care folosim format (f)
print(f"Si este inmatriculata pe numele meu: {inmatriculata}") # string + boolean -> folosim format (f)

print("---------------------------------6------------------------------------")


"""
6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
"""

nume = input("Introduceti numele: ")
prenume = input("Introduceti prenumele: ")
print(f"Ati introdus : {nume} {prenume}")
nume_complet = nume + prenume # concatenam 2 string-uri, fara spatii
print(f"Numele complet are {len(nume_complet)} caractere")

print("---------------------------------7------------------------------------")

"""
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
"""

lungimea = int(input("Introduceti lungimea dreptunghiului: ")) # "fortam" citirea unui int
latimea = int(input("Introduceti latimea dreptunghiului: ")) # "fortam" citirea unui int
arie_dreptunghi = lungimea * latimea
print(f"Aria dreptunghiului este {arie_dreptunghi}")

print("---------------------------------8------------------------------------")

"""
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';
"""

propozitie = "Coral is either the stupidest animal or the smartest rock"
print(propozitie)
cuvantul_the = propozitie.split()
print(f"Cuvantul 'the' apare de {cuvantul_the.count('the')} ori in propozitie")
# print(f"Cuvantul 'the' apare de {propozitie.count(' the ')} ori in propozitie") - varianta simpla

print("---------------------------------9------------------------------------")

"""
9. Același string.
Inlocuieste cuvântul 'the' cu 'THE';
Printează rezultatul.
"""

print(propozitie.replace(" the ", " THE "))

print("---------------------------------10-----------------------------------")


"""
10. Același string.
Folosiți un assert ca să verificați dacă acest string conține doar numere.
"""

assert propozitie.isdigit() == False, "Codul se opreste aici, deoarece propozitia contine doar numere" # False == False -> evaluarea este True
print(f"Propozitia nu contine doar numere. Codul merge mai departe")

print("----------------------------------------------------------------------")
