#aluguel de carros

#quantos km = R$0.15 por km rodado
#quantos dias = 60 reais dia
id = input('Qual seu nome?')
print('Bom dia,', id, '!')
dias = int(input('Quantos dias voce ficou com o carro?'))
km = float(input('Quantos km voce rodou com o carro?'))

#forma 1
total = (dias*60)+(km*0.15)
print('O valor a ser pago será de {}'.format(total))

#forma 2
vad = int(dias*60)
vakm = float(km*0.15)
vatotal = vad+vakm

print('O Sr. Passou {} dias com o carro, e andou {}km'.format(dias, km))
print('Totalizando um valor total por dias de R$:{:.2f},\num valor total por km de R$:{:.2f}\ne um valor total a ser pago de R${:.2f}.'.format(vad,vakm,vatotal))

print(id,',Obrigado por alugar conosco')