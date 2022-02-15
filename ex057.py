Sexo = str(input('Informe seu sexo: [M/F]')).strip()
while Sexo not in 'MmFf':
    Sexo = str(input('Dados inválido, Informe seu sexo: [M/F]'))
if Sexo in 'Mm':
    print('Sexo M registrado com sucesso')
if Sexo in 'Ff':
    print('Sexo F registrado com sucesso')
