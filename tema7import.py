from tema7 import *

patrat = Patrat()
patrat.descrie()
patrat.set_latura(6)
# patrat.set_latura(-6)
print(f"Latura patratului este {patrat.get_latura()}")
try:
    print(f"Aria patratului este {patrat.aria()}")
except TypeError:
    print("Ati introdus latura negativa")
patrat.delete_latura()
print(f"Latura patratului dupa stergere este {patrat.get_latura()}")
print("")

cerc = Cerc(4)
print(f"Raza cercului este {cerc.get_raza()}")
cerc.set_raza(6)
# cerc.set_raza(-6) # la setarea razei negative, ramane valoarea setata initial prin constructor
print(f"Raza cercului dupa set este {cerc.get_raza()}")
print(f"Aria cercului este {cerc.aria()}")
cerc.delete_raza()
print(f"Raza cercului dupa delete este {cerc.get_raza()}")
cerc.descrie()

