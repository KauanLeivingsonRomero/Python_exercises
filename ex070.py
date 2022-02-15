print('-' * 24)
print('   LOJA SUPER BARATÃO')
print('-' * 24)
nome = ' '
total = caro = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto:'))
    preço = float(input('Preço: R$'))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    total += preço
    cont += 1
    if preço > 1000:
        caro += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    if continuar in 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
