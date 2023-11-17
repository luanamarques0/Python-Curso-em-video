salario = float(input("Qual o salário do funcionario? R$"))
print(f"Um funcionário que ganhava R${salario}, com aumento de 15 %, passa a receber R${salario + (salario * (15/100)):.2f}")