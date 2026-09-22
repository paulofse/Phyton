#conversor de temperatura

while True:
    res = input('Qual temperatura voce quer converter? \n Celcius(C) \n Farenheit(F) \nDigite:')

    if res.upper()== 'C':
        print('Conversão de Celsius para Fahrenheit')
        Temc = float(input('QUal a temperatura atual em Celcius'))
        Tempct = float((Temc*9/5)+32)
        print('{} Graus em Celcius equivalem a {:.1f} Graus Farenheits'.format(Temc, Tempct))
        break

    elif res.upper() == 'F':
        print('Confersão de Fahrenheit para Celsius')
        Temf = float(input('QUal a temperatura atual em Fahreinheit'))
        Temft = float((Temf-32)*5/9)
        print('{} Graus em Farenheit equivalem a {:.1f} Graus Celcius'.format(Temf, Temft))
        break

    else:
        print('Resposta Invalida, Tente novamente!')


