nome = input("Digite seu nome: ")
nome = nome.upper()
nome = nome.find("SILVA")
if nome == 0:
    print("No seu nome tem SILVA")
else:
    print("No seu nome não tem SILVA")