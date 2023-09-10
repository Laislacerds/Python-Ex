salario = float(input('Digite o seu salario atual: R$'))

novo = salario + (salario * 15 / 100)

print('Você recebia o salario de {:.2f}R$ e passou a receber \n{:.2f}R$ de acordo com os 15% do reajuste salarial'.format(salario, novo))