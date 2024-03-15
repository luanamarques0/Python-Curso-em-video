salario = float(input("Digite seu salário: "))
if salario >= 1250:
    print(f"O salário agora é de: R$ {salario + (salario * 10 / 100):.2f}")
else:
    print(f"O salário agora é de: R$ {salario + (salario * 15 / 100):.2f}")