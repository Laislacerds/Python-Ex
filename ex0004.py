n1 = int(input('um valor:'))
n2 = int(input('Outro valor: '))

s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2

print('A soma é {}, a subtração é {} e a multiplicação é {}'.format(s, su, m)) #end='' para não pular linha.
print('A divisão é {:.1f}, e sua potência é {}'.format(d, e))
