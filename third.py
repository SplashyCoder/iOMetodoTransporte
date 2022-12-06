import numpy as np

matrix_1 = np.array([
        ['A',['1',5],['2',6],['3',3],['4',10],['5',7],1000],
        ['B',['1',8],['2',9],['3',6],['4',4],['5',4],600],
        ['C',['1',6],['2',7],['3',6],['4',10],['5',8],500],    
        ['D',['A',500],['B',100],['C',600],['D',300]],    
        ])

matrix_1_numericas = np.array([5,6,3,10,7,8,9,6,4,4,6,7,6,20,8])

matrix_1_numericas_sorted = np.sort(matrix_1_numericas)
index_1 = matrix_1_numericas_sorted[0]
index_2 = matrix_1_numericas_sorted[1]
index_3 = matrix_1_numericas_sorted[2]
index_4 = matrix_1_numericas_sorted[3]
index_5 = matrix_1_numericas_sorted[4]
index_6 = matrix_1_numericas_sorted[5]
index_7 = matrix_1_numericas_sorted[6]


apuntador = np.where(matrix_1 == index_1)

first = index_1*600
second = index_2*300
third = index_3*200
fourth = index_4*400
fifth = index_5 * 100
sixth = index_5 * 100
# seventh = index_5 * 18


suma = first + second + third + fourth + fifth + sixth

print('')
print('granja/almacen   1            2        3            4          5          6           oferta')
print('   A            5(400)        6      3(600)        10          7          0             0')
print('   B            8(100)        9        6          300(4)     4(200)       0             0')
print('   C             6          7(100)     6           10          8          0             0')
print('demanda          0            0        0            0          0')
print(suma)