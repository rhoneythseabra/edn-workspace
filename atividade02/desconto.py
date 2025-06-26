prod = str(input("Informe o produto: "))
preco = float(input("Informe o preço: "))
desconto = float(input("Qual o desconto: "))

valor_desconto = preco * desconto / 100
valor_final = preco - valor_desconto

print(f"{prod} de valor R$:{preco:.2f}, com o desconto de {desconto}%, tem o valor final de: R${valor_final:.2f}.")