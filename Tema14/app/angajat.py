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
        return self.nume + " " + self.prenume
        # return self.nume, self.prenume # daca pun asa se va returna un tuplu si se vor putea folosi separat

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu = self.salariu + (self.salariu * (procent/100))
        return self.salariu