import numpy as np

matrix_1 = np.array([
        [1,['A',5],['B',6],['C',5.4],400],
        [2,['A',7],['B',4.6],['C',6.6],500],
        [3,['A',200],['B',400],['C',300],700],    
        ])

matrix_1_numericas = np.array([5,6,5.4,7,4.6,6.6])

matrix_1_numericas_sorted = np.sort(matrix_1_numericas)
index_1 = matrix_1_numericas_sorted[0]
index_2 = matrix_1_numericas_sorted[1]
index_3 = matrix_1_numericas_sorted[2]
index_4 = matrix_1_numericas_sorted[3]


apuntador = np.where(matrix_1 == index_1)

first = index_1*200
second = index_2*400
third = index_3*200
fourth = index_4*100

suma = first + second + third + fourth

print('EJEMPLO 1')
print('granja/almacen   SAN ANTONIO  HOT SPRINGS  SOUX FALLS  oferta')
print('PHOENIX            5(200)           6         5,4(200)    0')
print('ATLANTA              7           4,6(400)     6,6(100)    0')
print('demanda              0             0            0         0')
print(suma)


