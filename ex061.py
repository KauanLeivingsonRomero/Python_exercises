print('Gerador de PA')
print('-=' * 7)
pt = int(input('Primeiro Termo:'))
razao = int(input('Razão: '))
termo = pt
c = 0
while c < 10:
    print('{}'.format(termo), end=' -> ')
    termo += razao
    c += 1
if c == 10:
    print('Acabou')