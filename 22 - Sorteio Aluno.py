#sorteio entre 4 alunso para apagar o quadro
import random
#import os
#os.system('color')

prof = input('Qual seu nome professor')

print('boa tarde, professor {}.'.format(prof))
while True:
        print('--- NOVO SORTEIO ---')
        al1 = input('Qual nome do primeiro aluno?')
        al2 = input('Qual nome do segundo aluno?')
        al3 = input('Qual nome do terceiro aluno?')
        al4 = input('Qual nome do quarto aluno?')

        print('O nome dos quatro alunos são:{},{},{} e {}'.format(al1,al2,al3,al4))
        lista = [al1,al2,al3,al4]
        sorteado = random.choice(lista)
        print('O aluno sorteado foi \033[1;31m{}\033[m'.format(sorteado))

