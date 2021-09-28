#Um robo de combate só deve ativar sua arma principal
#quando o inimigo esta menos de 70cm de distancia.Faça um programa onde o usuario informe a distancia do inimigo
#e sejam exbididas as mensagens 'ATIVO ou 'DESATIVO' dependendo do status da arma

distancia = float(input('Digite a distancia do inimigo'))

if distancia < 70:
    print('ARMA ATIVADA')
else:
    print('ARMA DESATIVADA')