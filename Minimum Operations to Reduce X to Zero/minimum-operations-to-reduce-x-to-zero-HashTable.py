class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums)<x:return -1
        hasht={0:-1}
        length=len(nums)

        leftsum,rightsum=0,0
        for i in range(length):                       # Time Complexity O(N)
            leftsum+=nums[i]                          # Space Complexity O(N)
            hasht[leftsum]=i
            
        result=float('inf')
        
        if x in hasht:result= hasht[x]+1

        for i in range(length):
            rightsum+=nums[length-i-1]
            if x-rightsum in hasht:
                result=min(i+hasht[x-rightsum]+2,result)
        
        if result==float('inf'):return -1
        else: return result
