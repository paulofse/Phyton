#exercicio 23

num = str(input('Digite um numero de 0 a 9999'))
print('O numero escolhido é: {}'.format(num))

sep = str(' '.join(num))
lista = sep.split()
#print(lista)

print('metodo de lista:')
print('unidade:', lista[3])
print('dezenas:', lista[2])
print('centenas:', lista[1])
print('milhar:', lista[0])

print('metodo de posição de caracteres:')
print('unidade:',num[3])
print('dezena:',num[2])
print('centena:',num[1])
print('milhar:',num[0])

num2 = int(input('Digite um numero de 0 a 9999'))
u = num2 // 1 % 10
d = num2 // 10 % 10
c = num2 // 100 % 10
m = num2 // 1000 % 10
print('A unidade digitado foi {}'.format(u))
print('A dezena digitado foi {}'.format(d))
print('A centena digitado foi {}'.format(c))
print('A milhar digitado foi {}'.format(m))