nome = str(input("Digite seu nome completo: ")).strip()
nome_final = nome.split()

print(f"Seu primeiro nome é: {nome_final[0]}")
print(f"Seu último nome é: {nome_final[-1]}")