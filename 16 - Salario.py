#Salario funcionário

sal = float(input('qual o seu salario?'))
print('hoje o salario do funcionario é {}'.format(sal))
aum = float(input('qual o aumento do salario em %?'))
aumL = sal*aum/100
print('o valor do aumento será R$:{:.2f}.'.format(aumL))
salt = sal + aumL
print('O valor total final do salario depois do aumento será R$:{:.2f}.'.format(salt))

print('Obrigado e bom trabalho!')