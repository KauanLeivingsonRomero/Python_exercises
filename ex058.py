from random import randint
from time import sleep
print('Sou seu computador...')
sleep(2)
print('Vou pensar em um número entre 0 e 10.')
sleep(2)
print('Você consegue adivinhar ?')
sleep(1.5)
palpite = int(input('Qual é o seu palpite? '))
computador = randint(1, 10)
tentativas = 0
while palpite != computador:
    if palpite <= computador:
        palpite = int(input('Mais... tente novamente.'))
        tentativas += 1
    elif palpite >= computador:
        palpite = int(input('Menos... tente novamente.'))
        tentativas += 1
if palpite == computador:
    tentativas += 1
print('Acertou com {} tentativas. Parábens'.format(tentativas))
