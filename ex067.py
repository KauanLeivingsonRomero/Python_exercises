print(f'-' * 15)
print(f'    TABUADA')
print(f'-' * 15)
while True:
    n = int(input(f'Quer ver a tabuada de qual número ? \n[\033[32mNúmero negativo encerra o programa\033[m]'))
    if n < 0:
        break
    print(f'-' * 15)
    for c in range(1, 11):
        r = n * c
        print(f'{n} x {c} = {r}')
    print('-' * 15)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
