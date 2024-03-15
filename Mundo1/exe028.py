import random

numero = random.radint(1, 5) 
numero_usuario = int(input("Em que númro eu pensei?"))
if numero == numero_usuario:
    print("Parabéns, você venceu!")
else:
    print("Eu venci!")


