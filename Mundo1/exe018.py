import math
angulo = float(input("Digite o ângulo: "))
radianos = math.radians(angulo)
print(f"O ângulo de {angulo} tem o seno de {math.sin(radianos):.2f}")
print(f"O ângulo de {angulo} tem o cosseno de {math.cos(radianos):.2f}")
print(f"O ângulo de {angulo} tem a tangente de {math.tan(radianos):.2f}")
#Poderia ter sido feito assim: math.tan(math.radians(angulo)), em vez de criar outra variável