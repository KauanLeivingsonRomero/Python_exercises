completa = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    completa.append([nome, [nota1, nota2], media])
    quantidade = enumerate(completa)
    continuar = str(input('Quer continuar:')).upper().strip()
    if continuar in 'S':
        continue
    if continuar in 'N':
        break
print('-' * 30)
print(f'{"Nº"} {"Nome":<10} {"Média":>8}')
print('-' * 26)
for i, a in enumerate(completa):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? [999 interrompe]:'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(completa) - 1:
        print(f'Notas de {completa[opc][0]} são {completa[opc][1]}')
print('<<<  VOLTE SEMPRE  >>>')
