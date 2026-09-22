tam = int(input('Qual a tamanho em metros? '))
cen = tam*100
mil = tam*1000
# eu poderia usar so a quebra \n para separar as linhas nao precisaria fazer 3 prints no caso
print('O Tamanho em metros é:', tam)
print('O tamanho em centimetro é:', cen)
print('O tamanho em milimetros é:', mil)
#exemplo de print limpo
print('{}m, Equivale a {}cm e {}mm' .format (tam, cen, mil))
#exemplo de print limpo
print('O tamanho em metros é:', tam,'(m)''\nO tamanho em centimetros é:', cen,'(cm)''\nO tamanho em milimetros é:', mil,'(mm)')

print('Obrigado')
