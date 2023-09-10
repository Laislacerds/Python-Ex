preço = float(input('Digite o preço do produto: R$'))

novo = preço - (preço * 5 / 100)

print('O produto custava {}, na promoção com o desconto de 5% passou a custar R${}'.format(preço, novo))