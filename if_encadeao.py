idade = int(input('Por favor, didgite sua idade!'))

if idade<16:
    print('Voce ainda nao pode votar')
else:
    if idade>=18:
        print('Voce é obrigado a votar')
    else:
        print('Voce pode optar por votar')