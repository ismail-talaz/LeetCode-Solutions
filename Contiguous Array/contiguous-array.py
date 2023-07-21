class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix={0:-1}
        currSum=0
        maxL=0

        for i,num in enumerate(nums):
            if num:currSum+=1
            else:currSum-=1

            if currSum in prefix:
                maxL=max(maxL,i-prefix[currSum])
            else: prefix[currSum]=i
        
        return maxL
