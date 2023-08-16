class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1               # Time Complexity O(logn)

        while (right-1>left): 

            mid=(left+right)//2                          
            
            if nums[left]>nums[mid]:
                right=mid
            else:
                left=mid
        if nums[right]>nums[left]:return nums[0]
        else:return nums[right]
