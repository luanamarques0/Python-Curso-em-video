distandica_da_viagem = float(input("Digite a distância da viagem em KM: "))
if distandica_da_viagem <= 200:
    print(f"O valor da viagem vai custar: R$ {distandica_da_viagem * 0.50:.2f}")
else:
    print(f"O valor da viagem vai custar: R$ {distandica_da_viagem * 0.45:.2f}")