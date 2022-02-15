from random import randint
print('=-' * 13)
print('Vamos jogar par ou ímpar')
print('=-' * 13)
cont = 0
while True:
    n = int(input('Digite um valor: '))
    j = ' '
    while j not in 'PI':
        j = str(input('Par ou ímpar [P/I]:')).upper().strip()[0]
    computador = randint(0, 10)
    total = n + computador
    if j == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            print(f'Você jogou {n} e o computador {computador}. o total deu {total} PAR')
            cont += 1
        else:
            print('Você perdeu')
            print(f'Você jogou {n} e o computador {computador}. o total deu {total} ÍMPAR')
            break
    elif j == 'I':
        if total % 2 == 0:
            print('Você perdeu')
            print(f'Você jogou {n} e o computador {computador}. o total deu {total} PAR')
            break
        if total % 2 == 1:
            print('Você ganhou')
            print(f'Você jogou {n} e o computador {computador}. o total deu {total} ÍMPAR')
            cont += 1
    print('Vamos jogar novamente')
print(f'Você ganhou {cont} vezes')
