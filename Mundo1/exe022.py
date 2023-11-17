nomeCompleto = input("Digite seu nome completo: ").strip()

print("Todas as letras em maiúsculas: " ,nomeCompleto.upper())
print("Todas as letras em minúsculas: " ,nomeCompleto.lower())
#print(f"O seu nome tem {len(nomeCompleto) - nomeCompleto.count(' ')} letras.")
#print(f"O primeiro nome tem {nomeCompleto.find(' ')} letras.")
nome = nomeCompleto.split()
nome1 = "".join(nome)

print("O seu nome tem ", len(nome1), "letras.")
print("O primeiro nome tem ", len(nome[0]), "letras.")

