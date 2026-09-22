from xml.dom.minidom import ProcessingInstruction
#com variavel pra puxar depois
n1 = int(input('Digite um Numero!'))
print('O primeiro numero escolhido foi {}'.format(n1))
na = n1+1
nan = n1-1
print('O Antecessor de {} é {} e o sucessor de {} é {} .'.format(n1, nan,n1, na))
#pra uso unico
n2 = int(input('Digite um Numero!'))
print('O segundo numero escolhido foi {}'.format(n2))

print('O Antecessor de {} é {} e o sucessor de {} é {} .'.format(n1, n1 - 1, n1, n1 + 1))
print('O Antecessor de {} é {} e o sucessor de {} é {} .'.format(n2, n2 -1, n2, n2 + 1))