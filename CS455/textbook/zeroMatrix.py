'''
1.8 zeroMatrix

Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.

'''
def zeroMatrix(matrix):
    row = []
    col = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)
                
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in row or j in col:
                matrix[i][j] = 0
                    
                    
test = [[1,1,1],[1,0,1],[1,1,1]]
test2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

zeroMatrix(test)
zeroMatrix(test2)
print(test)
print(test2)
