class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        rowzero=0
        colzero=0

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if i==0:rowzero=1
                    if j==0:colzero=1
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j] == 0 or matrix[i][0]==0:
                    matrix[i][j]=0
        if rowzero:
            for j in range(n):
                matrix[0][j]=0
        if colzero:
            for i in range(m):
                matrix[i][0]=0
