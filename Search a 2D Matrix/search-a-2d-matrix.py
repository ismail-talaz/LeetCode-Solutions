class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n=len(matrix)
        m=len(matrix[0])
        left,right=0,m*n-1                     # Time Complexity O(log(m*n))

        while (left<=right):
            mid=(left+right)//2
            row=mid//m
            col=mid%m

            if matrix[row][col]==target:
                return True

            if matrix[row][col]<target:
                left=mid+1
            else:
                right=mid-1

        return False
