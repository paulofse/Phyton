din = float(input('Quanto de dinheiro voce tem?'))
moe = input('Qual moeda voce quer comprar?')
dol = float(input('Quanto ta a cotação atual de 1 {}? R$:'.format(moe)))
#dol = 3.27

tot = float(din/dol)

print('De acordo com o que voce tem na carteira R$:{}, Voce pode comprar {:.2f} {}'.format(din, tot,moe))

#quando começar aprender api fazer esse lcodigo buscando os valores na internet
