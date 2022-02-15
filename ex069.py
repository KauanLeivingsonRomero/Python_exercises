cont = conthomem = contmulher = 0
while True:
    print('-' * 23)
    print('  CADASTRE UMA PESSOA')
    print('-' * 23)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] ')).upper().strip()[0]
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    if sexo in 'F' and idade <= 20:
        contmulher += 1
    if sexo in 'M':
        conthomem += 1
    if idade >= 18:
        cont += 1
    if opcao in 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {conthomem} homens cadastrados ')
print(f'E temos {contmulher} com menos de 20 anos')
