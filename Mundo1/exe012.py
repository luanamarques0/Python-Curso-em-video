preco = float(input("Qual preço do produto? R$"))
print(f"O produto custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${preco - (preco * (5/100)):.2f}")