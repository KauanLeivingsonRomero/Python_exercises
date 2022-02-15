print('-' * 23)
print('Sequência de Fibonacci ')
print('-' * 23)
termos = int(input('Quantos termos você quer mostrar?'))
pn = 0
sn = 1
print('{} -> {}'.format(pn, sn), end='')
contador = 3
while contador <= termos:
    tn = pn + sn
    print(' -> {}'.format(tn), end='')
    pn = sn
    sn = tn
    contador += 1
print(' Final')
