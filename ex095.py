time = []
gols = []
dados = {}
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    time.append(dados.copy())
    while True:
        continuar = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar in 'S':
        continue
    if continuar in 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador [999 para parar]:'))
    if busca == 999:
        break
    if busca >= len(dados):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} --')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print(' VOLTE SEMPRE')
