cid = str(input('Digite o nome da cidade')).strip()#pedindo o nome da cidade
#procurando por santo em minusculo no inicio da frase
low = cid.lower()
#print(low, ' - nome da cidade em minusculo')
#print('santo' in low, ' - existe santo no nome da cidade?')
sanl = low[0:5]
torfl = 'santo' in sanl
print(torfl, ' - começa com santo!', '#independente se o usuario digitar maiuscula ou minuscula se iniciar por santo ele acusa true!')

#procutando por santo em maiusculo no inicio da frase
hig = cid.upper()
#print(hig, ' - nome da cidade em minusculo')
#print('santo' in hig, ' - existe santo no nome da cidade?')
sanh = hig[0:5]
torfh = 'SANTO' in sanh
print(torfh, ' - começa com SANTO!', '#independente se o usuario digitar maiuscula ou minuscula se iniciar por santo ele acusa true!')

SAN = cid[:5]
san = cid[:5]
toh = 'SANTO' in SAN
tou = 'santo' in san
print(toh, ' - começa com SANTO?', '#so acusa TRUE se iniciar exatamente com SANTO!')
print(tou, ' - começa com santo?', '#so acusa TRUE se iniciar exatamente com santo!')
