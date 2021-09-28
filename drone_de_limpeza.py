#Um drone de limpeza de ruas deve escolher carregar sempre o lixo menor peso.
#Entre os pesos de 3 lixos informados pelo usuário, um programa deve idicar qual deles seve ser carregados pelo drone

print('DRONE DE LIMPEZA')


lixo1 = float(input('Digite o peso do lixo 1'))
lixo2 = float(input('Digite o peso do lixo 2'))
lixo3 = float(input('Digite o peso do lixo 3'))

if lixo1 < lixo2 and lixo1 < lixo3:
    print('Recolher o lixo 1')
elif lixo2 < lixo1 and lixo2 < lixo3:
    print('Recolher o lixo 2')
elif lixo3 < lixo1 and lixo3 < lixo2:
    print('Recolher o lixo 3')
else:
    print('Existem lixos com o mesmo peso. Contate o suporte!')
