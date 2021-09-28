print("Programa calculador de idade")

nascimento = int(input('Por favor digite seu ano de nascimento'))

idade = 2021 - nascimento

print('A sua idade parece ser {} anos.'.format(idade))

if idade>=18:
    print('Voce é maior de idade!')
else:
    print('Voce é menor de idade!')