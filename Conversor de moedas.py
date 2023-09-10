real = float(input('Digite quanto dinheiro você tem: R$'))
dolar1 = float(input('Digite quanto de dinheiro você tem: US$'))


dolar = real / 4.91
real2 = dolar1 * 0.20

print('\n')

print('Com R${} você consegue comprar {:.2f}US$'.format(real, dolar))
print('Com US${} você consegue comprar {:.2f}R$'.format(dolar1, real2))
