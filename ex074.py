from random import randint
aleatórios = (randint(1, 10), randint(1, 10), randint(1, 10),
              randint(1, 10), randint(1, 10))
print('Valores sorteados:', end='')
for n in aleatórios:
    print(f'{n} ', end='')
print(f'\nO maior valor foi {max(aleatórios)}')
print(f'E o menor valor foi {min(aleatórios)}')
