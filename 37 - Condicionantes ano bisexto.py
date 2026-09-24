import datetime
while True:
    print('olá, sera que o ano é bisexto?')
    bis = int(input('Qual ano voce quer saber?'))

    if bis == 0:
        bis = datetime.date.today().year
    if bis % 4 == 0 and bis % 100 != 0 or bis % 400 == 0:
        print('O ano {} é bisexto!'.format(bis))
    else:
        print('O ano {} nao é bisexto!'.format(bis))

