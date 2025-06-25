peso = float(input('Informe o seu peso em kg: '))
altura = float(input('Informe sua altura em metros: '))

imc = float(peso / (altura * altura))

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")    
else:
    print("Obeso")    