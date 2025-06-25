idade = int(input('Digite uma idade: '))

if idade <= 0:
    print('Idade inválida!')
elif idade <= 13:
    print('Você é uma criança!')
elif idade <= 17:
    print('Você é um(a) adolescente!')
elif idade <= 59:
    print('Você é um(a) adulto!')
elif idade >= 60:
    print('Você é um(a) idoso(a)!')    
