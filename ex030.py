r1 = float(input('comprimento reta 1 CM:'))
r2 = float(input('comprimento reta 2 CM:'))
r3 = float(input('comprimento reta 3 CM:'))

if (r1 + r2 >= r3 and r2 +r3 >= r1) and r1 + r3 >= r2:
    print('PODEMOS FORMAR UM TRIÂNGULO')
else:
    print('NÃO PODEMOS FORMAR UM TRIÂNGULO')