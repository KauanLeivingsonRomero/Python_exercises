print('Gerador de PA')
print('-=' * 7)
pt = int(input('Primeiro Termo:'))
razao = int(input('Razão: '))
termo = pt
c = 1
total = 0
pergunta = 10
while pergunta != 0:
    total = pergunta
    while c <= total:
        print('{}'.format(termo), end=' -> ')
        termo += razao
        c += 1
    print('Pausa')
    pergunta = int(input('Quantos termos você quer mostra a mais?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))
