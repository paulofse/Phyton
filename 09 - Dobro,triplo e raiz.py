n1 = int(input('Digite um Numero!'))
#dobro
d = n1 * 2
#triplo
t = n1 * 3
#raizquadrada
r = n1 ** (1/2)
print('O numero escolhido foi {}'.format(n1))
print('O dobro de {} é {}.\nO triplo de {} é {}.\nA raiz quadrada de {} é {:.2f}.' .format(n1, n1*2, n1, n1*3,n1, n1**(1/2)))
print('O dobro de {} é {}, O triplo de {} é {} A raiz quadrada de {} é {:.2f}.' .format(n1,d, n1, t,n1,r))