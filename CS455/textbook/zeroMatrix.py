'''
1.8 zeroMatrix

Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.

'''

def zeroMatrix(matrix):
    
    row = []
    col = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)
                
    for x in range(len(matrix)):
        matrix[x][j] = 0
    for y in range(len(matrix[0])):
        matrix[i][y] = 0                  
    return matrix








''' 
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                column.append(j)
                row.append(i)
                
    for i in range(len(matrix)):
        for j in column:
            matrix[i][j] == 0
    for i in row:
        for j in range(len(matrix[0])):
            matrix[i][j] == 0
'''
test = [[1,1,1],[1,0,1],[1,1,1]]
test2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

zeroMatrix(test)
zeroMatrix(test2)
print(test)
print(test2)