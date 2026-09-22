#soma 5+2 ==
#subtração 5-2 ==
#Multiplicação 5*2 ==
#Divisão 5/2 ==
#Potencia 5**2 ==
#Divisão Inteira 5//2 ==
#Resto da divisão 5%2 ==

n1 = int(input('Digite um Numero:'))
n2 = int(input('digite outro Numero:'))

s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
f = n1 // n2
i = n1 % n2

print('A soma é {}, A Multiplicação é {}, A divisão é {:.2f}, a potencia é {}'.format(s, m, d, e), end=' ')
print('divisoes inteira {} e resto {}' .format(i, f))

