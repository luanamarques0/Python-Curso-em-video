frase = str(input("Digite uma frase: ")).lower().strip()

print(f"A letra 'A' aparece {frase.count('a') + 1}")
print(f"A primeira letra 'A' apareceu na posição: {frase.find('a') + 1}")
print(f"A última letra 'A' apareceu na posição: {frase.rfind('a') + 1}")