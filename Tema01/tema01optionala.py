                        ##### Exercitii optionale #####

print("---------------------------------1------------------------------------")

"""
1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
"""

cuvant = input("Introduceti un cuvant cu nr. impar de caractere: ")
if len(cuvant) % 2 != 0: # daca restul impartirii (modulo %) lungimii cuvantului la 2 este diferit de 0 -> nr. impar de caractere
    print(f"Ati introdus: {cuvant}")
    mijloc = len(cuvant) // 2 # impartim la 2 lungimea cuvantului folosind floor division (//) care ne rotunjeste in jos spre un nr. intreg
    # print(mijloc)
    print(f"Caracterul din mijlocul cuvantului '{cuvant}' este: '{cuvant[mijloc]}'") # accesam caracterul cu index-ul 'mijloc'
else:
    print("Cuvant invalid. Cuvantul introdus are nr. par de caractere.")

"""
ex: Cuvant      s  a  p  t  e
    Index       0  1  2  3  4
len(sapte) -> 5
5//2 = 2
caracterul din mijloc va fi pe pozitia 2
"""

print("---------------------------------2------------------------------------")

"""
2. Folosind assert, verifică dacă un string este palindrom.
"""

text = input("Introduceti un cuvant: ")
print(f"Cuvantul scris normal: {text[:]}")
print(f"Cuvantul scris invers: {text[::-1]}")

palindrom = text[:] == text[::-1] # daca e palindrom, returneaza True
#print(palindrom)

assert palindrom == True, "Cuvantul nu este palindrom" # True == True -> evaluarea este True
print("Cuvantul introdus este palindrom")

print("---------------------------------3------------------------------------")

"""
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
"""

string1, string2 = input("Introduceti doua cuvinte cu spatiu intre ele: ").split()
print(f"Primul cuvant introdus este: {string1}")
print(f"Al doilea cuvant introdus este: {string2}")

print("---------------------------------4------------------------------------")

"""
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
"""

string_1 = input("Introduceti un text: ")
first = string_1[0] # prima litera din string
middle = string_1[1:-1] # string-ul fara prima si ultima litera
last = string_1[-1] # ultima litera din string
# print(first) # prima litera din string
# print(middle) # string-ul fara prima si ultima litera
# print(last) # ultima litera din string
middle = middle.replace(first, first.upper()) # inlocuim prima litera a string-ului in mijlocul lui si suprascriem variabila
string_1_new = first + middle + last # concatenam pentru a forma noul string
print(string_1_new)

print("---------------------------------5------------------------------------")

"""
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
"""
user = input("Introduceti user-ul: ")
parola = input("Introduceti parola: ")
parola_ascunsa = len(parola) * "*"
print(f"Parola pt. user '{user}' este {parola_ascunsa} si are {len(parola)} caractere")


