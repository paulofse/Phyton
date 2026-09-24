import random
import time
print('Seja bem vindo!')
nome = str(input('Qual o seu nome?')) .upper()
print('O jogo funciona da seguinte forma {}, eu vou escolher um numero entre 0 e 5 e voce tem que acertar, Simples Assim!' .format(nome))

n = random.randint(0,5)
#print('O numero era {}!'.format(n))
nu = int(input('Escolha seu numero entre 0 e 5:'))
print('Loading...')
time.sleep(3)
if n == nu:
    print('Meus parabens {} voce gastou a sua sorte com besteira, da proxima vez jogue na mega sena!'.format(nome))
else:
    print('aproveita que nao ganhou {} e nao gastou a sorte, pra jogar na mega sena!'.format(nome))

print('O numero era {}!'.format(n))

print('===FIM DE JOGO====')