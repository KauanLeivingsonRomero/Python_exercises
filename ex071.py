print('-' * 24)
print('    CAIXA ELETRÔNICO')
print('-' * 24)
valor = int(input('Qual o valor a ser sacado ? R$'))
total = valor
dinheiro = 50
quantidade = 0
while True:
    if total >= dinheiro:
        total -= dinheiro
        quantidade += 1
    else:
        if quantidade > 0:
            print(f'Total de {quantidade} cédulas de {dinheiro}')
        if dinheiro == 50:
            dinheiro = 20
        elif dinheiro == 20:
            dinheiro = 10
        elif dinheiro == 10:
            dinheiro = 1
        quantidade = 0
        if total == 0:
            break
print('Volte sempre')