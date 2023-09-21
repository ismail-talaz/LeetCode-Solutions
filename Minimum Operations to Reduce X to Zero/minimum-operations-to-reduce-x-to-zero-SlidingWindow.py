class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        length=len(nums)
        if length==1: return 1 if nums[0]==x else -1
        if sum(nums)<x: return -1

        start,end,maximum=0,1,-1                               # Time Complexity O(N)
        currsum=nums[0]                                        # Space Complexity O(1)
        target=sum(nums)-x
        if currsum==target:maximum=1

        while end<length:
            currsum+=nums[end]
            end+=1
            
            while currsum>target:
                currsum-=nums[start]
                start+=1
            
            if currsum==target:
                maximum=max(end-start,maximum)

        
        return length-maximum if maximum!=-1 else -1
