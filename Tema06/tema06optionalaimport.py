from tema06optionala import *

print("---------------------------------1------------------------------------")

factura_cumparaturi = Factura(22, "Samsung", 4, 5000)
factura_cumparaturi.genereaza_factura()
factura_cumparaturi.schimba_cantitatea(5)
factura_cumparaturi.schimba_pretul(6500)
factura_cumparaturi.schimba_nume_produs("iPhone")
print("\n")
factura_cumparaturi.genereaza_factura()

print("---------------------------------2------------------------------------")

masina = Masina("A4", 240)

masina.descrie()
print("\n")
masina.inmatriculare()
masina.vopseste("crem")
# masina.vopseste("neagra")
# masina.accelereaza(-30)
masina.accelereaza(280)
# masina.accelereaza(140)
# masina.franeaza()
print("\n")
masina.descrie()

print("---------------------------------3------------------------------------")

todo = TodoList()

todo.adauga_task("Cumparaturi_Mega", "Cumpara Cola")
todo.adauga_task("Cumparaturi_Carrefour", "Cumpara Cips")
todo.adauga_task("Cumparaturi_Lidl", "Cumpara Cartofi")
todo.adauga_task("Arunca_cojile", "Du gunoiul")
todo.afisare()
print("\n")
todo.finalizeaza_task("Cumparaturi_Carrefour")
todo.afisare()
print("\n")
todo.afiseaza_todo_list()
print("\n")
todo.afiseaza_detalii_suplimentare('Arunca_cojile')
print("\n")
todo.afiseaza_detalii_suplimentare('Fugi_la_Mega')
todo.afisare()