#Programa pra ler o comprimento do co e ca de um triangulo e calcular a hipotenusa
import math
print('olá')
nome = input('Qual seu nome?')
print('Opa {}, vamos calcular a hipotenusa do nosso triangulo retangulo' .format(nome))

co = float(input('Digite o valor do Cateto Oposto:'))
ca = float(input('Digite o valor do Cateto Adjacente:'))

hi = math.sqrt((co ** 2) + (ca ** 2))
hi2 = ((co ** 2) + (ca ** 2))**(1/2)

print('O valor da Hipotenusa é {}'.format(hi))
print('O valor da Hipotenusa é {}'.format(hi2))