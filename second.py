import numpy as np

matrix_1 = np.array([
        [1,['A',10],['B',2],['C',20],['D',11],15],
        [2,['A',12],['B',7],['C',9],['D',20],25],
        [3,['A',4],['B',14],['C',16],['D',18],10], 
        [4,['A',50],['B',15],['C',15],['D',15]],    
        ])

matrix_1_numericas = np.array([10,2,20,11,12,7,9,20,4,14,16,18])

matrix_1_numericas_sorted = np.sort(matrix_1_numericas)
index_1 = matrix_1_numericas_sorted[0]
index_2 = matrix_1_numericas_sorted[1]
index_3 = matrix_1_numericas_sorted[2]
index_4 = matrix_1_numericas_sorted[3]
index_5 = matrix_1_numericas_sorted[4]


apuntador = np.where(matrix_1 == index_1)

first = index_1*5
second = index_2*15
third = index_3*15
fourth = index_4*10
fifth = index_5 * 18

suma = first + second + third + fourth + fifth

print('')
print('granja/almacen   A          B         C         D           oferta')
print('   1            10        2(15)      20        11              0')
print('   2            12          7       15(9)    10(20)            0')
print('   3           (5)4        14        16      15(18)            0')
print('demanda          0          0         0         0')
print(suma)


