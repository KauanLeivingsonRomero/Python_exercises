lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número:'))
    continuar = str(input('Quer continuar [S/N]:')).upper().strip()
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    if n % 2 == 1:
        impares.append(n)
    if continuar in 'S':
        continue
    if continuar in 'N':
        break
print('-=' * 29)
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')
