dados = []
nomeepeso = []
maior = menor = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    nomeepeso.append(nome)
    nomeepeso.append(peso)
    if len(dados) == 0:
        maior = menor = nomeepeso[1]
    else:
        if nomeepeso[1] > maior:
            maior = nomeepeso[1]
        if nomeepeso[1] < menor:
            menor = nomeepeso[1]
    dados.append(nomeepeso[:])
    nomeepeso.clear()
    continuar = str(input('Quer continuar [S/N]:')).upper().strip()
    if continuar in 'S':
        continue
    if continuar in 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(dados[:][0])} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. peso de ', end='')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
