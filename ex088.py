from time import sleep
from random import randint
print('-' * 30)
print('      JOGO DA MEGA SENA')
print('-' * 30)
lista = []
jogos = []
cont = 0
numeros = randint(1, 60)
jogadas = int(input('Quantos jogos você quer que sorteie? '))
tot = 1
while tot <= jogadas:
    cont = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {jogadas} JOGOS', '-=' * 3)
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('-=' * 5, '< BOA SORTE >', '-=' * 5)
