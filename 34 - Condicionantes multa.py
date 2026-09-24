print('Bom dia')
vel = float(input('Qual a velocidade do carro?'))
if vel < 80:
    print('Voce estava a {}Km/h e dentro do limite de velocidade, Parabens voce é um motorista conciente!'.format(vel))
else :
    print('É o que amigo? {}km/h sua velocidade excedeu o limite de 80km/h'.format(vel))
    multa = (vel - 80) * 7
    print('Voce recebeu uma multa de R${:.2f}'.format(multa))
print('Aproveite para refletir sobre o caso e tenha um bom dia')