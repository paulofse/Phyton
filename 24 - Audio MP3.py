import os
import time
import pygame

user = input('Qual seu nome?')
print('boa tarde! {}, Vamos ouvir uma musica?'.format(user))

pygame.init()
# 1. Inicializa o motor de áudio
pygame.mixer.init()
while True:
   print('='*40)
# 2. O Python busca na pasta juntando o ".mp3" automaticamente nos bastidores
   pfmusic = os.listdir('musicas')
   print('Buscando musicas na pasta...')
   print('Musicas listadas: {}'.format(pfmusic))

# 3. Pergunta direta (o usuário digita apenas o nome, ex: "rock")
   play = input('Qual o nome da musica voce quer ouvir?')

# --- PASSO NOVO: CHECAGEM PARA SAIR ---
   if play == 'sair':
       print('\nObrigado por usar o reprodutor, {}! Até a próxima. 👋'.format(user))
       break  # Desliga o while na hora e fecha o programa!

# 4. Carrega a música juntando a pasta, o nome digitado e a extensão .wav
   pygame.mixer.music.load('musicas/' + play + '.wav')

# 5. Mostra a mensagem de confirmação automática que você queria
   print('\n[CONFIRMADO] Entendido! Tocando agora: {}.wav 🎵'.format(play))

# 6. Dá o play automático no som
   pygame.mixer.music.play()

# Trava o terminal aberto para a música continuar saindo nas caixas de som
   input('\nPressione ENTER para encerrar o reprodutor...')






#todar diretamente no play de forma simples.
#pygame.init() #iniciando o pygame
#pygame.mixer.init() #iniciando motor de audio
#pygame.mixer.music.load('musicas/mu1.wav') #escolhendo, carregando e tocando a musica escolhida
#pygame.mixer.music.play()#tocando
#while pygame.mixer.music.get_busy():
    #pass





