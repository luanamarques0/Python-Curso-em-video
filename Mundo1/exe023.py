numero = input("Digite um número: ")
if numero[3] == "":
  print("unidade: 0")
else:
  print("unidade:", numero[3])
if numero[2] == "":
  print("dezena: 0")
else:
  print("dezena:", numero[2])
if numero[1] == "":
  print("centena: 0")
else:
  print("centena:", numero[1])
if numero[0] == "":
  print("milhar: 0")
else:
  print("milhar:", numero[0])

# numero = int(input())
# print(f"Unidade: { numero // 1 % 10 }")
# print(f"Dezena: { numero // 10 % 10 }")
# print(f"Centena: { numero // 100 % 10 }")
# print(f"Milhar: { numero // 1000 % 10 }")


