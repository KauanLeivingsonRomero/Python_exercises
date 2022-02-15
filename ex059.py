from time import sleep

primeirovalor = int(input('Primeiro valor:'))
segundovalor = int(input('Segundo valor:'))
continuar = False
while not continuar:
    print('-=' * 12)
    print(''' [ 1 ] Soma
 [ 2 ] Multiplicar
 [ 3 ] Maior
 [ 4 ] Novos números
 [ 5 ] Sair do programa''')
    print('-=' * 12)
    opcao = int(input('Qual sua opcao?'))
    if opcao == 1:
        adicao = primeirovalor + segundovalor
        print('{} + {} é = {}'.format(primeirovalor, segundovalor, adicao))
    if opcao == 2:
        multiplicar = primeirovalor * segundovalor
        print('{} x {} = {}'.format(primeirovalor, segundovalor, multiplicar))
    if opcao == 3:
        if primeirovalor < segundovalor:
            print('{} é maior que {}'.format(segundovalor, primeirovalor))
        else:
            print('{} é maior que {}'.format(primeirovalor, segundovalor))
    if opcao == 4:
        primeirovalor = int(input('Primeiro valor:'))
        segundovalor = int(input('Segundo valor:'))
    if opcao == 5:
        continuar = True
        print('Finalizando...')
        sleep(2)
    if opcao > 5:
        print('Opção inválida. tente novamente')
        primeirovalor = int(input('Primeiro valor:'))
        segundovalor = int(input('Segundo valor:'))
    elif opcao < 1:
        print('Opção inválida. tente novamente')
        primeirovalor = int(input('Primeiro valor:'))
        segundovalor = int(input('Segundo valor:'))
