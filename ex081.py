lista = []
cont = 0
continuar = ''
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    cont += 1
    continuar = str(input('Quer continuar [S/N]:')).upper().strip()
    if continuar in 'S':
        continue
    else:
        break
print('-=' * 25)
print(f'Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não foi encontrado na lista!')