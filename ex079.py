lista = []
continuar = ''
while True:
    n = int(input('Digite um valor:'))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!...')
    else:
        print('Valor duplicado! Não adicionado.')
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar == 'S':
        continue
    if continuar == 'N':
        break
print('-=' * 19)
lista.sort()
print(f'Você digitou os valores {lista}')
