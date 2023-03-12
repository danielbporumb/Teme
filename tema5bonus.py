                    ##### Exercitii bonus #####

"""
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""

print("---------------------------------1------------------------------------")

def numere_comune(lista1, lista2):
    comune = set()
    for i in lista1: # parcurgem cele doua liste
        for j in lista2:
            if i == j:
                comune.add(i)
    return comune


lista1 = [1, 3, 2, 5, 6, 7, 9, 12, 3]
lista2 = [3, 5, 7, 9, 10, 2, 4, 6, 1]
print(f"Elementele comune din cele doua liste sunt : {numere_comune(lista1, lista2)}")

"""
2. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
"""

print("---------------------------------2------------------------------------")

def reducere_pret(pret_produs, reducere):
        # if reducere in range(0, 100):
        #     print("Reducere invalida")
        # else:
            pret_final = pret_produs - (pret_produs * (reducere/100))
            return pret_final


pret_produs = float(input("Introduceti pretul produsului : "))
reducere = int(input("Introduceti reducerea in % pentru produs : "))
if reducere in range(0, 100):
    print(f"Pretul final al produsului este de {reducere_pret(pret_produs, reducere)} lei")
else:
    print("Reducere invalida")

# am tratat cazurile de 'reducere invalida' si in afara functiei, deoarece am vrut sa nu imi mai afiseze in acest caz
# si "Pretul final al produsului este de None lei"

"""
3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)
"""

print("---------------------------------3------------------------------------")

import datetime
import pytz   # am gasit pe net ca aceasta ar fi libraria pentru python time zone

# zona = pytz.all_timezones
# print(zona)

def data_ora_curenta(time_zone):
    zona = pytz.timezone(time_zone)
    data_ora = datetime.datetime.now(zona)
    data_ora = data_ora.strftime("%d.%m.%Y  -  %H:%M:%S  -  %Z") # am gasit pe net cum se formateaza cu strftime()
    return data_ora


print(f"Data si ora in Romania: {data_ora_curenta(time_zone='Europe/Bucharest')}")
print(f"Data si ora in China:   {data_ora_curenta(time_zone='Asia/Hong_Kong')}")

"""
4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
"""

print("---------------------------------4------------------------------------")

# def zile_pana_la(data_definita):
#     data_definita = datetime.datetime.strptime(data_definita, '%Y-%m-%d').date() # am vazut ca python returneaza data sub forma : YYYY-MM-DD asa ca am formatat la fel datele de intrare
#     print(f"Ati introdus : {data_definita}")
#     data_curenta = datetime.date.today() # luam data curenta
#     print(f"Data curenta : {data_curenta}")
#     urmatoarea_data = datetime.date(data_curenta.year, data_definita.month, data_definita.day) # luam urmatoarea data din anul curent cu ziua si luna din cele introduse
#     # print(f"Urmatoarea data : {urmatoarea_data}")
#     if urmatoarea_data < data_curenta: # daca a trecut data adaugam un an la urmatoarea data
#         urmatoarea_data = datetime.date(data_curenta.year + 1, data_definita.month, data_definita.day)
#     zile_ramase = (urmatoarea_data - data_curenta).days # punem .days sa afiseze in zile
#     return zile_ramase
#
#
#
# data_definita = (input("Introdu anul-luna-ziua :"))
# print(f"Pana la ziua mea mai sunt {zile_pana_la(data_definita)} zile")

def zile_pana_la(data_definita):
    data_definita = datetime.datetime.strptime(data_definita, '%Y-%m-%d').date() # am vazut ca python returneaza data sub forma : YYYY-MM-DD asa ca am formatat la fel datele de intrare
    print(f"Ati introdus : {data_definita}")
    data_curenta = datetime.date.today() # luam data curenta
    print(f"Data curenta : {data_curenta}")
    zile_ramase = (data_definita - data_curenta).days # punem .days sa afiseze in zile
    return zile_ramase

data_definita = (input("Introdu anul-luna-ziua :"))

if zile_pana_la(data_definita) < 0:
    print(f"Au trecut {abs(zile_pana_la(data_definita))} zile de la ziua mea")
else:
    print(f"Pana la ziua mea mai sunt {zile_pana_la(data_definita)} zile")