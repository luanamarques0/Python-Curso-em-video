velocidade_do_carro = int(input("Qual a velocidade do carro?"))

if velocidade_do_carro <= 80:
    print("Dirija  com segurança!")
else:
    print(f"Velocidade acima do permitido, A multa vai custar R$7,00 por cada Km acima do limite.\nSua multa é de: R${(velocidade_do_carro  - 80) * 7:.2f}")