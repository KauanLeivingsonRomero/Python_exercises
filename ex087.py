matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somatc = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
        if n % 2 == 0:
            soma += n
        somatc = matriz[0][2] + matriz[1][2] + matriz[2][2]
        for p in matriz[1][:]:
            if p == 0:
                maior = p
            else:
                if p > maior:
                    maior = p
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {somatc}')
print(f'O maior valor da segunda linha é {maior}')
