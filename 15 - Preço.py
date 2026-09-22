print('ola, hoje nós estamos com uma otima promoção!')

pro = input('qual produto voce gostaria de analisar')
pr = float(input('qual o preço da etiqueta?'))
nt = float(pr-pr*5/100)
print('hoje nós temos 5% de desconto para pagamentos a vista!')
print('O preço final do seu', pro, 'será:{:.2f}'.format(nt), end='')
print('  Obrigado e volte sempre!!')

