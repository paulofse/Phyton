#sen cos e tang

import math
from math import radians, sin, cos, tan
print('olá')
nome = input('Qual seu nome?')
print('Opa {}, vamos calcular o Sen, Cos e Tang do nosso Angulo' .format(nome))

angulo = float(input('Qual seu angulo?'))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
#sin2 = math.sin(angulo)
#cos2 = math.cos(angulo)
#tan2 = math.tan(angulo)

print('O valor do Sen = {:.2f}, do Cos = {:.2f} e da Tang {:.2f}, Obrigado!'.format(sen, cos, tan))
print('O valor do Sen = {:.2f}, do Cos = {:.2f} e da Tang {:.2f}, Obrigado!'.format(math.ceil(sen),math.ceil(cos),math.ceil(tan)))
print('Os valores Arredondados sao respectivamente {},{},{}'.format(math.ceil(sen),math.ceil(cos),math.ceil(tan)))
