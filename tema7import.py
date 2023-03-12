from tema7 import *

patrat = Patrat()
patrat.descrie()
patrat.latura_set(6)
# patrat.latura_set(-6)
print(f"Latura patratului este {patrat.latura_get()}")
try:
    print(f"Aria patratului este {patrat.aria()}")
except TypeError:
    print("Ati introdus latura negativa")
patrat.latura_delete()
print(f"Latura patratului dupa stergere este {patrat.latura_get()}")
print("")

cerc = Cerc(4)
print(f"Raza cercului este {cerc.raza_get()}")
cerc.raza_set(6)
# cerc.raza_set(-6) # la setarea razei negative, ramane valoarea setata initial prin constructor
print(f"Raza cercului dupa set este {cerc.raza_get()}")
print(f"Aria cercului este {cerc.aria()}")
cerc.raza_delete()
print(f"Raza cercului dupa delete este {cerc.raza_get()}")
cerc.descrie()

