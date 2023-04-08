                    ##### Exercitii obligatorii #####

"""
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’

INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)

Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată

Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)

POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
"""

from abc import ABC, abstractmethod

# ABSTRACTION  /  ABSTRACTIZARE

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi")

# INHERITANCE / MOSTENIRE

class Patrat(FormaGeometrica):
    __latura = None

    # def __int__(self, latura):
    #     self.__latura = latura

#  ENCAPSULATION / INCAPSULARE

    def get_latura(self):
        return self.__latura

    def set_latura(self, latura):
        if latura <= 0:
            print("Latura nu poate fi negativa")
        else:
            self.__latura = latura

    def delete_latura(self):
        self.__latura = None

    def aria(self):
        return self.__latura **2

class Cerc(FormaGeometrica):
    __raza = None

    def __init__(self, raza):
        self.__raza = raza

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        if raza <= 0:
            print("Raza nu poate fi negativa")
        else:
            self.__raza = raza

    def delete_raza(self):
        self.__raza = None

    def aria(self):
        return self.__raza **2 * self.PI

    def descrie(self):
        print("Eu nu am colturi")

