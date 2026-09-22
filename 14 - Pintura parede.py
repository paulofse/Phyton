print('Bem vindo ao ajudante de obras')

meA = float(input('Primeiro me diga a altura da parede em metros:'))
print('A altura da parede em metros é {}'.format(meA))
meL = float(input('Agora preciso saber a largura da parede em metros:'))
print('A largura da parede em metros é {}'.format(meL))
Arp = meA * meL
Tin = 2

print('A area da parede é:', Arp,"m²")
Li = Arp/Tin
print('Dimensões: {}x{}, logo a Area total é {:.2f}m²'.format(meA,meL,Arp))

print('Agora considerando que cada litro de tinta pinta uma area de 2m²,\n'
      'para pintar essa parede precisaremos de',Li, ' litros de tinta')


