valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}:')))
print('-=' * 25)
print(f'Você digitou os valores {valores}')
print(f'O maior valor foi {max(valores)} nas posições ', end='')
for p, n in enumerate(valores):
    if n == max(valores):
        print(f'{p}... ', end='')
print()
print(f'O menor valor foi {min(valores)} nas posições ', end='')
for p, n in enumerate(valores):
    if n == min(valores):
        print(f'{p}... ', end='')
print()
