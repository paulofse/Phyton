print('DIA DE AUMENTO')
SAL = float(input('Digite o salario do funcionario: '))
print('para salarios até R$: 1250 aumento de 15% acima disso 10% de aumento!')
if SAL > 1250:
    salf = SAL + float(SAL*0.10)
    print('O seu aumento será de 10%')
else:
    salf = SAL + float(SAL * 0.15)
    print('O seu aumento será de 15%')

print('o salario final é R$: {} '.format(salf))


