extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20:'))
    while n > 20 or n < 0:
        n = int(input('Tente novamente. Digite um número entre 0 e 20:'))
    print(f'Você digitou o número {extenso[n]}')
    continuar = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if continuar in 'S':
        n = int(input('Digite um número entre 0 e 20:'))
        while n > 20 or n < 0:
            n = int(input('Tente novamente. Digite um número entre 0 e 20:'))
        print(f'Você digitou o número {extenso[n]}')
        continuar = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if continuar in 'N':
        break
print('-=' * 9)
print('Fim do programa')
print('-=' * 9)

