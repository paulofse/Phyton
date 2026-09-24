print('DIA DO TRIANGULO: ')
print('Agora digite o valor dos 3 lados do triangulo')
l1 = int(input('Digite o comprimento do primeiro lado: '))
l2 = int(input('Digite o comprimento do segundo lado: '))
l3 = int(input('Digite o comprimento do terceiro lado: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Sim os lados formam um triangulo')
else:
    print('Não, os lados não formam um triangulo')

print('EASY')