from tema06 import *

print("---------------------------------1------------------------------------")

raza_cerc = int(input("Introduceti raza cercului : "))
culoare_cerc = input("Introduceti culoarea cercului : ")

cerc = Cerc(raza_cerc, culoare_cerc)

cerc.descriere_cerc()
print(f"Cercul are diametrul = {cerc.diametru()}")
print(f"Cercul are aria = {cerc.aria()}")
print(f"Cercul are circumferinta = {cerc.circumferinta()}")

print("---------------------------------2------------------------------------")

lungime_dreptunghi = int(input("L = "))
latime_dreptunghi = int(input("l = "))
culoare_dreptunghi = input("Introduceti culoarea dreptunghiului : ")

dreptunghi = Dreptunghi(lungime_dreptunghi, latime_dreptunghi, culoare_dreptunghi)

dreptunghi.descrie()
print(f"Aria dreptunghiului = {dreptunghi.aria()}")
print(f"Perimetrul dreptunghiului = {dreptunghi.perimetrul()}")
dreptunghi.schimba_culoarea("rosu")
print(f"\nDupa schimbarea culorii : ")
dreptunghi.descrie()

print("---------------------------------3------------------------------------")

electrician = Angajat("Popescu", "Mihai", 2300)
electrician.descrie()
# print(f"Numele complet al angajatului : {electrician.nume_complet()}")
nume, prenume = electrician.nume_complet() # daca le-am definit in clasa la acea metoda ca si tuplu, le initializam si aici la fel
print(f"Numele angajatului este {nume} {prenume}") # si le putem folosi separat
print(f"Salariul acestuia este de {electrician.salariu_lunar()} lei pe luna")
print(f"Salariul acestuia pe un an este de {electrician.salariu_anual()}")
procent_marire = int(input("Introduceti procentul maririi salariale : "))
print(f"Salariul acestuia dupa marire este de {electrician.marire_salariu(procent_marire)} lei")
# dupa mariri
# print(f"Salariul acestuia este de {electrician.salariu_lunar()} lei pe luna")
# print(f"Salariul acestuia pe un an este de {electrician.salariu_anual()}")
print("---------------------------------4------------------------------------")

salariat = Cont("RO12TRLD64265498428", "Popa Mircea", 4000)
salariat.afisare_sold()
scoate_bani = int(input("Retragere numerar : "))
if scoate_bani in range(salariat.sold):
    salariat.debitare_cont(scoate_bani)
else:
    print("Fonduri insuficiente. Reincercati.")
    scoate_bani = int(input("Retragere numerar : "))
    salariat.debitare_cont(scoate_bani)
salariat.afisare_sold()
baga_bani = int(input("Depunere numerar : "))
salariat.creditare_cont(baga_bani)
salariat.afisare_sold()
