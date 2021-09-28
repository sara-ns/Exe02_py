# Em uma loja para que sejam concedidos descontos de 5% é
#necessario que o valor  total da compra seja superior a R$1000 e
#que o comprador use o cupom "CUPOM5

print('BLOWSTORE')

total_compra = float(input('Por favor digite o total da compra'))
cupom = input('Por favor digite o seu cupom')

#O in, utilizado abaixo, verifica se o texto "CUPOM5" esta dentro da variavel
#(mesmo que ele contenha outros textos alem dessee)
if total_compra>1000 and 'CUPOM5' in cupom.upper():
    valor_compra = total_compra * 0.95

#A informação :.2f faz com que o valor a ser exibido mostre 2 casas decimais
print('O valor da compra é de R${:.2f}'.format(total_compra))