n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n Multiplicação{} e A divisão {:.3f}'.format(s, m, d), end=' ')
print('Divisao inteira {}, Potencia {}'.format(di, e))