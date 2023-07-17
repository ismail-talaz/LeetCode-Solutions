class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum=count=0
        sums={0:1}

        for i in range(len(nums)):
            currSum+=nums[i]

            if currSum-k in sums:
                count+=sums[currSum-k]

            if currSum in sums:
                sums[currSum]+=1
            else: sums[currSum]=1
        
        return count