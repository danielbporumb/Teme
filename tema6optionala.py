                    ##### Exercitii optionale #####

"""
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
"""

class Factura:
    seria = 825
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate
        # print(f"Noua cantitate: {self.cantitate}")

    def schimba_pretul(self, pret):
        self.pret_buc = pret
        # print(f"Noul pret: {self.pret_buc}")

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        # print(f"Noul produs: {self.nume_produs}")

    def genereaza_factura(self):
        from datetime import date
        print(f"Factura seria {Factura.seria} numar {self.numar}\n"
              f"Data:{date.today()}")
        print("|{0:^13} | {1:^13}|  {2:^13} | {3:^13} |".format("Produs", "cantitate", "pret bucata", "Total"))
        print("|{0:^13} | {1:^13}|  {2:^13} | {3:^13} |".format(self.nume_produs, self.cantitate, self.pret_buc, self.cantitate * self.pret_buc))


"""
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
"""

class Masina:
    marca = "Audi"
    model = None
    viteza_maxima = None
    viteza_actuala = 0
    culoare = "gri"
    culori_disponibile = {"verde", "albastra", "rosie", "neagra", "visinie", "argintie"}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f"Masina marca '{self.marca} {self.model}', de culoare {self.culoare}\n"
              f"Viteza maxima constructiva : {self.viteza_maxima} km/h\n"
              f"Este inmatriculata : {self.inmatriculata}\n"
              f"Are viteza actuala : {self.viteza_actuala} km/h")

    def inmatriculare(self):
        self.inmatriculata = True
        print("Masina a fost inmatriculata")

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
            print(f"Masina a fost vopsita in culoarea {culoare}")
        else:
            print(f"Culoarea {culoare} nu este disponibila")


    def accelereaza(self, viteza):
        if viteza < 0:
            print("Viteza necorespunzatoare")
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
            print(f"Viteza mai mare decat viteza constructiva a masinii. Am accelerat la {self.viteza_maxima}")
        else:
            self.viteza_actuala = viteza
            print(f"Am accelerat la {self.viteza_actuala}")

    def franeaza(self):
        self.viteza_actuala = 0
        print("Am oprit masina")


"""
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:
● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
"""

class TodoList:
    todo = dict()

    def adauga_task(self, nume, descriere):
        # self.nume = input("Introdu numele task-ului : ")
        # self.descriere = input("Introdu descrierea task-ului : ")
        self.nume = nume
        self.descriere = descriere
        self.todo[self.nume] = self.descriere
        print(f"A fost adaugat task-ul '{self.nume} : {self.descriere}'")

    def finalizeaza_task(self, nume):
        self.todo.pop(nume)
        print(f"Task-ul '{nume}' a fost finalizat")

    def afiseaza_todo_list(self):
        print(f"Task-urile pe scurt :")
        for key in self.todo.keys():
            print(key)

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task not in self.todo:
            print(f"Task-ul {nume_task} nu se afla pe lista.")
            raspuns = input("Doriti sa-l adaugati? \n")
            if str(raspuns).lower() == "nu":
                print("La revedere")
            elif str(raspuns).lower() == "da":
                descriere_task = input("Introdu descrierea task-ului : ")
                self.todo[nume_task] = descriere_task
            else:
                print("Raspuns invalid. Raspundeti cu 'da' sau 'nu'")
        else:
            print(f"Detalii suplimentare task : {self.todo[nume_task]}")

    def afisare(self): # am mai facut eu pentru test aceasta metoda, ca sa pot vedea mereu intreg dict-ul
        print(f"TodoList:\n"
              f"{self.todo}")

