numeros = [[], []]
n = 0
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor:'))
    if n % 2 == 0:
        numeros[0].append(n)
    if n % 2 == 1:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print('-=' * 30)
print(f'Todos os valores: {numeros}')
print(f'Os números pares são {numeros[0]}')
print(f'Os números ímpares são {numeros[1]}')
