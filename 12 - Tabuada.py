tab = int(input(' Diga qual o numero voce quer saber a tabuada: '))
#forma 1 direta
print(tab,'x 1 =', tab*1)
print(tab,'x 2 =', tab*2)
print(tab,'x 3 =', tab*3)
print(tab,'x 4 =', tab*4)
print(tab,'x 5 =', tab*5)
print(tab,'x 6 =', tab*6)
print(tab,'x 7 =', tab*7)
print(tab,'x 8 =', tab*8)
print(tab,'x 9 =', tab*9)
print(tab,'x 10 =', tab*10)

print('_'*40)


#forma2

print('{}x{:2}={:2}'.format(tab,1,tab*1))
print('{}x{:2}={:2}'.format(tab,2,tab*2))
print('{}x{:2}={:2}'.format(tab,3,tab*3))
print('{}x{:2}={:2}'.format(tab,4,tab*4))
print('{}x{:2}={:2}'.format(tab,5,tab*5))
print('{}x{:2}={:2}'.format(tab,6,tab*6))
print('{}x{:2}={:2}'.format(tab,7,tab*7))
print('{}x{:2}={:2}'.format(tab,8,tab*8))
print('{}x{:2}={:2}'.format(tab,9,tab*9))
print('{}x{:2}={:2}'.format(tab,10,tab*10))
print('_'*40)

#forma3

print('{}x{:2}={:2}''\n{}x{:2}={:2}''\n{}x{:2}={:2}''\n{}x{:2}={:2}''\n{}x{:2}={:2}''\n{}x{:2}={:2}''\n{}x{:2}={:2}''\n{}x{:2}={:2}''\n{}x{:2}={:2}''\n{}x{:2}={:2}'.format(tab,1,tab*1,tab,2,tab*2,tab,3,tab*3,tab,4,tab*4,tab,5,tab*5,tab,6,tab*6,tab,7,tab*7,tab,8,tab*8,tab,9,tab*9,tab,10,tab*10))
print('_'*40)
#varios format? inviavel...mas util se necessario
#print( tab,'x {} = {}\n'.format(1,tab*1),tab,'x {} = {}\n'.format(2,tab*2))



print(' Essa é a tabuada de {}, Muito obrigado, até a proxima!' .format(tab))

