dados = {}
gols = []
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for i, v in dados.items():
    print(f'O campo {i} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for c, v in enumerate(dados['gols']):
    print(f'   => Na partida {c}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols')
