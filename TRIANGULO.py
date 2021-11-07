L1 = float(input('Digite o primeiro L:'))
L2 = float(input('Digite o segundo L:'))
L3 = float(input('Digite o terceiro L:'))

if L1 < L2 + L3 and L1 < L3 + L2 and L3 < L1 + L2:
        print('Show, formou um TRIÂNGULO', end=' ')
        if L1 == L2 == L3:
                print('EQUILÁTERO: {},{},{}'.format(L1,L2,L3))
        elif L1 != L2 !=L3 !=L1:
                print("ESCALENO: {},{},{} ".format(L1,L2,L3))
        else:
                print('ISÓCELES: {}, {}, {}'.format(L1,L2,L3))
else:
        print("Infelizmente não forma TRIÂNGULO")
