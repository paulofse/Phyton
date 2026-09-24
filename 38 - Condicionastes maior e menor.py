num1 = int(input('Digite um numero inteiro:'))
num2 = int(input('Digite outro numero inteiro:'))
num3 = int(input('Digite outro numero inteiro:'))
print('Os numeros escohidos foram: {}, {}, {}'.format(num1, num2, num3))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num3 and num2 > num1:
    maior = num2
else:
    maior = num3
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num3 and num2 < num1:
    menor = num2
else:
    menor = num3



print('O maior numero é: {}'.format(maior))
print('O menor numero é: {}'.format(menor))

print('obrigado')