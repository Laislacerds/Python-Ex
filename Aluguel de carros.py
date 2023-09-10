D = int(input('Digite a quantidade de dias que ele foi alugado: '))
km = float(input('Digite a quantidade de km percorridos: '))

pago = (D * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(pago))
