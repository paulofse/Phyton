frase = 'Curso em video python'
print(frase)

print(frase[9],' - é o  caractere escolhido') #exibe um caractere especifico.
print(frase[9:21],' - é o intervalo escolhido') #exibe um intervalo.
print(frase[9:21:2],' - é o intervalo com saltos escolhido') #exibe um intervalo saltando de 2 em 2.
print(frase[:5],' - intervalo iniciando do caractere zero') #exibe um intervalo do inicio '0' ao caractere '5'.
print(frase[15:], ' - intervalo iniciando no caractere quinze') #exibe um intervalo do caractere '15' ao ultimo .
print(frase[9::3], ' - intervalo iniciando no caractere 9 até o fim de 3 em 3') #exibe um intervalo do caractere '9' ao ultimo pulando de 3 em 3.
print(frase[::2], ' - do inicio ao fim de 2 em 2') #exibe um intervalo do inicio '0' ao fim pulando de 2 em 2.

len(frase) #comprimento
print(len(frase), ' - quantos caracteres existem na frase')

lo = frase.count('o') #contar quantas letras o minusculo tem no texto.
print(frase.count('p'),' - quantidade da letras p escolhida')
print(lo, ' - quantidade da letras o escolhida')

deo = frase.find('deo') #achar trecho do texto, na posição que o trecho começa.
print(deo, ' - o trecho começa nessa posição, se for negativo nao existe') #quando retornar valor -1(negativo) significa que dentro do intervalo nao existe o solicitado
print(frase.find('deo'), ' - o trecho começa nessa posição, se for negativo nao existe')
cur = 'curso' in frase #essa opção devolve verdadeiro ou falso a find devolve o posicionamento ou -1
print(cur, ' - essa opção informa a existencia ou nao da sequencia de caracteres')
print('curso' in frase, ' - essa opção informa a existencia ou nao da sequencia de caracteres')

#troca de uma palavra por outra no resultado, nao troca na string original
android = frase.replace('python', 'android')
print(android)
print(frase.replace('python', 'android'))

#tudo maiusculo
maiusculas = frase.upper()
print(frase.upper())
print(maiusculas)

#tudo maiuscul separado
maisp = frase.upper().split()
print(frase.upper().split())
print(maisp)

#tudo minusculo
minusculas = frase.lower()
print(frase.lower())
print(minusculas)

#tudo minusculo separado
minsp = frase.lower().split()
print(frase.lower().split())
print(minsp)


parag = frase.capitalize()
titulo = frase.title()
print(parag, ' - tudo minusculo somente a primeita letra da string maiuscula')
print(frase.capitalize())
print(titulo, ' - todas as primeiras letras de todas as palavras mausculas')
print(frase.title())

#tratando os espaços das frases
frase2 = '   aprenda python  '
print(frase2)
print(frase2.strip())
print(frase2.lstrip()) #remove os espaços do lado esquerdo l = left
print(frase2.rstrip()) #remove os espaços do lado direito r = right

uniao = ' '.join(frase)
print(uniao) #com variavel
print(' '.join(frase))
print('-'.join(frase))

print('-'.join(maisp))
print('-'.join(minsp))

print(""" SERVE PRA VOCE DIGITAR TEXTOS LONGOS""")