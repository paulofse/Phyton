frase = str(input('Digite uma frase: ')).lower().strip()
#frase
#frasel = frase.lower() #frase minuscula
letra = str(input('Digite uma letra da frase: ')).lower().strip()#letra
#letral = letra.lower() #letra minuscula

la = frase.count(letra) #contar na frase minuscula a quantidade de letra minuscula
print('quantidade de {} letras -{}- na frase'.format(la,letra)) #exibir resultado
#print('quantidade de {} letras -{}- na frase'.format(frase.count(letra),letra)) #exibir resultado
ffa = frase.find(letra) #achar a primeira letra
flu = frase.rfind(letra) #achar a ultima letra
print('A primeira letra ta no caractere {} e a Ultima no caractere {}, assim entende o python'.format(ffa,flu))
print('A primeira letra ta no caractere {} e a Ultima no caractere {}, assim entende o usuario'.format(ffa+1,flu+1))