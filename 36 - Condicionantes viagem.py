via = float(input('ola, qual a distancia que pretende viajar?'))
temp = via / 80 #descobrindo o tempo

if temp <1: #se o tempo for menor que 1
    temp1 = str(temp*60) + 'min' #ele da o tempo arredonda e diz que sao minutos
else:
    temp1 = str(temp) + 'h' #ele da o tempo  e diz que sao horas


print('Sua viagem terá {}km '.format(via,))
if via < 200:
    pas1 = float(via * 0.50)
    print('Sua passagem será R${:.1f} e terá uma duração de aproximadamente {}'.format(pas1, temp1))

else :
    pas1 = float(via * 0.45)
    print('Sua passagem será R${:.1f} e terá uma duração de aproximadamente {}'.format(pas1, temp1))

print('Obrigado por viajam com PYTHON')


#preço = via * 0.50 if distancia <= 200 else distancia 0.45
#simplificado