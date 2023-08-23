class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        cols=[]

        for i in range(m):
            row_will_be_zero=0
            for j in range(n):
                if matrix[i][j]==0:
                    cols.append(j)
                    row_will_be_zero=1
                if j==n-1 and row_will_be_zero:
                    matrix[i]=[0]*n
        
        for i in range(m):
            for j in cols:
                matrix[i][j]=0
