                    ##### Exercitii obligatorii #####


"""
1. Obligatoriu UNIT TESTS pt ex2 - clasa Dreptunghi
● Clasa Dreptunghi
● Atribute: lungime, latime, culoare
● Constructor pt toate atributele
● Metode:
● descrie()
● aria()
● perimetrul()
● schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
Ea va lua ca si param o noua culoare si va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().

1. Unit tests pt toate metodele
● Cum poti testa totusi schimba culoarea daca nu returneaza nimic?
● Fie verificati direct valoarea atributului, fie verif ce returneaza metoda
descrie()

OPTIONAL (sau dupa terminarea cursului pentru a extinde framework de unit
tests)
- Unit tests pt clasele Cerc, Cont si Angajat
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
