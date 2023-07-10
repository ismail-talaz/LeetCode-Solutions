class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        length=len(nums)
        
        if length==1 or nums[0]>nums[1]:return 0
        elif nums[length-1]>nums[length-2]:return length-1

        while (left<=right):
            mid=(left+right)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:return mid
            elif nums[mid]>nums[mid+1]:right=mid-1
            else: left=mid+1