class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=0
        maxSum=0                       # Kadene's Algorithm
        for i in range(len(nums)):
            currSum=max(nums[i],currSum+nums[i])
            maxSum=max(currSum,maxSum)
        
        return maxSum
