total_compra = float(input('Informe o total da compra'))
cupom = input('Informe o cupom')

if 'cupom5' not in cupom.lower():
    total_compra = total_compra * 0.95
print('O total a ser pago é R${:.2f}'.format(total_compra))