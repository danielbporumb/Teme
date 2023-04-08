                    ##### Exercitii obligatorii #####

"""
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
"""

class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f"Descriere cerc:\n"
              f"Cercul are raza {self.raza}\n"
              f"Cercul are culoarea {self.culoare}")

    def aria(self):
        pi = 3.14
        aria = pi * self.raza**2
        return aria

    def diametru(self):
        d = 2 * self.raza
        return d

    def circumferinta(self):
        pi = 3.14
        c = 2 * pi * self.raza
        return c

"""
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul 
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
"""

class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"Descriere dreptunghi: \n"
              f"Are lungimea = {self.lungime}\n"
              f"Are latimea = {self.latime}\n"
              f"Are culoarea {self.culoare}")

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return 2*(self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


"""
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""

class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, bani):
        self.nume = nume
        self.prenume = prenume
        self.salariu = bani

    def descrie(self):
        print(f"Angajat:\n"
              f"Nume : {self.nume}\n"
              f"Prenume : {self.prenume}\n")

    def nume_complet(self):
        # return self.nume + " " + self.prenume
        return self.nume, self.prenume # daca pun asa se va returna un tuplu si se vor putea folosi separat

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu = self.salariu + (self.salariu * (procent/100))
        return self.salariu


"""
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""

class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul '{self.titular_cont}' are in contul cu IBAN: {self.iban} suma de {self.sold} lei")

    def debitare_cont(self, suma):
        self.sold -= suma
        print(f"Ati retras suma de {suma} lei")

    def creditare_cont(self, suma):
        self.sold += suma
        print(f"Ati depus suma de {suma} lei")





