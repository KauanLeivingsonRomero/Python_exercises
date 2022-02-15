times = ('São Paulo', 'Flamengo', 'Atlético-MG', 'Internacional',
         'Grêmio', 'Palmeira', 'Fluminense', 'Santos', 'Ceará SC',
         'Atlético-GO', 'Corinthians', 'Atlético-PR', 'Bragantino',
         'Fortaleza', 'Sport Recife', 'Bahia', 'Vasco da Gama',
         'Botafogo', 'Coritiba', 'Goiás')
print('-=' * 16)
print('Lista de Times do Brasileirão:', end='')
print(times[::])
print('-=' * 16)
print('Os primeiros 5 times são:', end='')
print(times[:5])
print('-=' * 16)
print('Os últimos 4 times são:', end='')
print(times[16:])
print('-=' * 16)
print('Times em ordem alfabética:', end='')
print(sorted(times))
print('-=' * 16)
print(f'O {times[10]} esta em 11ª posição')
