#programa que le o nome do usuario e retorna:
import random

nome = str(input ('Digite seu nome: ')).strip()
print('olá {}, seja bem vindo' .format(nome))
print('Segundo o exercicio:')
#nome com todas as letras maiusculas
#print(nome.upper(),'todas as letras maiusculas')
print('Seu nome em maiusculo é: {}'.format(nome.upper()))
#nome com todas as letras minusculas
#print(nome.lower(), 'todas as letras minusculas')
print('Seu nome em minusculo é: {}'.format(nome.lower()))

#quantidade de letras desconsiderando os espaços
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))
#print('*'.join(nome))
#print(nome.strip())
#print(len(nome.replace(' ', '')), 'letras no total (sem contar espaços)')
#print(len(''.join(nome.split())), 'letras no total (sem contar espaços)')
#quantas letras tem o primeiro nome

pnome = nome.split()
lista = list[str](pnome)
print('o seu primeiro nome é: {}! e tem {} letras'.format(lista[0], len(lista[0])))





