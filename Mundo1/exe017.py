import math
catetoOposto = float(input("Cateto oposto: "))
catetoAdjacente = float(input("Cateto adjacente: "))
print(f"A hipotenusa vai medir {math.hypot(catetoOposto, catetoAdjacente):.2f}")
