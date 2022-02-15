real = float(input('Quanto dinheiro vc tem na carteira? R$'))
dolar = real / 5.46
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
