continuar = 'S'
soma = media = quant = maior = menor = 0
while continuar in 'S':
    n = int(input('Digite um número:'))
    continuar = str(input('Quer continuar [S/N]:')).upper()
    quant +=1
    soma += n
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
