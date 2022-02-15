from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['carteira de trabalho'] = int(input('carteira de trabalho [0 não tem]:'))
if dados['carteira de trabalho'] == 0:
    print('-=' * 25)
    for i, v in dados.items():
        print(f' - {i} tem o valor {v}')
else:
    dados['ano de contratação'] = int(input('Ano de contratação:'))
    dados['salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['ano de contratação'] + 35) - datetime.now().year)
    print('-=' * 25)
    for i, v in dados.items():
        print(f' - {i} tem o valor {v}')
