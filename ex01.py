# O usuario digitara o peso de 2 caizas de uma linha de produçao
#Seu programa deve indicar qual delas sao mais pesada

caixa1= float(input('Digite o peso da primeira caixa'))
caixa2= float(input('Digite o peso da segunda caixa'))

if caixa1 > caixa2:
    print("A caixa 1 é a caixa mais pesada")
else:
    if caixa2 > caixa1:
        print('A caixa 2 é a caixa mais pesada')
    else:
        print('As duas caixas tem o mesmo peso')
    
