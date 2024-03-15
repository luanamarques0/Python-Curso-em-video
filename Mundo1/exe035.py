reta_1 = float(input("Primeira reta: "))
reta_2 = float(input("Segunda reta: "))
reta_3 = float(input("Terceira reta: "))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print("Os segmentos podem formar um triângulo!")
else:
    print("Os segmentos não podem formar um triângulo!")