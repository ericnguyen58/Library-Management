import numpy as np

def generate_pattern(row, column):
    matrix = np.zeros((row + 3, column + 3), dtype=int)
    for i in range(1, row + 3, 3):  
        for j in range(1, column + 3, 3):  
            matrix[i][j] = 1     
    return matrix

matrix = generate_pattern(10, 10)
print(matrix)