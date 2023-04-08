                    ##### Exercitii optionale #####

"""
1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
- Declara o lista cu 5 jucatori: lista_jucatori_teren
- Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
- Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
- Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
- SCHIMBARI_MAX va fi o constanta cu valoarea 3
Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
- Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
teren
- Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
- Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
de rezerva
- Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
variabilelor voastre)
Daca jucatorul pe care vrem sa il schimbam nu e in teren:
- Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Altfel, afisati ecran: ‘mai aveti z schimbari’
"""

print("---------------------------------1------------------------------------")

lista_jucatori_teren = ['Hagi', 'Stanciu', 'Alibec', 'Budescu', 'Marica']
lista_jucatori_rezerva = ['Keseru', 'Dennis Man', 'Chiriches', 'Tanase', 'Coman']
lista_jucatori_scosi = []
SCHIMBARI_MAX = 3
schimbari_efectuate = 0 # z


while schimbari_efectuate < SCHIMBARI_MAX: # < 3; am pus totul intr-o instructiune repetitiva deoarece am vrut sa se ruleze codul pana se epuizeaza schimbarile
    jucatorul_care_iese = input("Introduceti jucatorul care iese : ")  # y
    jucatorul_care_intra = input("Introduceti jucatorul care intra : ")  # x
    if jucatorul_care_iese in lista_jucatori_teren: # daca jucatorul care trebuie scos este in teren
        if (jucatorul_care_intra in lista_jucatori_rezerva) and (jucatorul_care_intra not in lista_jucatori_teren): # daca cel ce intra este rezerva si nu este pe teren
            schimbari_efectuate+=1 # inseamna ca se poate face schimbarea
            lista_jucatori_teren.remove(jucatorul_care_iese) # cel ce iese se sterge din teren
            lista_jucatori_scosi.append(jucatorul_care_iese) # si se adauga in scosi
            lista_jucatori_teren.append(jucatorul_care_intra) # cel ce intra se adauga in teren
            lista_jucatori_rezerva.remove(jucatorul_care_intra) # si se scoate din rezerve
            schimbari_ramase = SCHIMBARI_MAX - schimbari_efectuate
            print(f"A intrat '{jucatorul_care_intra}', a iesit '{jucatorul_care_iese}'.\nSchimbari disponibile : {schimbari_ramase}")
            print(f"Pe teren sunt acum jucatorii : {lista_jucatori_teren}")
            print(f"Rezerve sunt acum jucatorii : {lista_jucatori_rezerva}")
            print(f"Pana cum au iesit jucatorii : {lista_jucatori_scosi}\n")
        elif jucatorul_care_intra in lista_jucatori_teren: # am mai pus niste conditii pt a afisa daca este deja in teren
            print(f"Jucatorul '{jucatorul_care_intra}' este deja in teren")
            print(f"Schimbari disponibile : {SCHIMBARI_MAX - schimbari_efectuate}\n") # am mai pus si aici scaderea pt a afisa in orice conditie cate schimbari sunt disponibile
        else:
            print(f"Jucatorul '{jucatorul_care_intra}' nu este rezerva") # si daca nu se afla printre rezerve
            print(f"Schimbari disponibile : {SCHIMBARI_MAX - schimbari_efectuate}\n")
    else:
        print(f"Nu se poate efectua schimbarea, deoarece jucatorul '{jucatorul_care_iese}' nu este in teren")
        print(f"Schimbari disponibile : {SCHIMBARI_MAX - schimbari_efectuate}\n")
print("S-a terminat numarul de schimbari permise")
