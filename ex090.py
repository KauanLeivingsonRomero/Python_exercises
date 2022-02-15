ficha = dict()
ficha['Nome'] = str(input('Nome: '))
ficha['Média'] = float(input('Média: '))
if ficha['Média'] >= 7:
    ficha['Situação'] = 'Aprovado'
if ficha['Média'] <= 5:
    ficha['Situação'] = 'Reprovado'
if 5 <= ficha['Média'] < 7:
    ficha['Situação'] = 'Recuperação'
print('-=' * 25)
for k, v in ficha.items():
    print(f' - {k}: {v}')
