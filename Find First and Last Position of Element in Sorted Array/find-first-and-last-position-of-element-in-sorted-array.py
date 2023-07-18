class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1

        while (left<=right):
            mid=(left+right)//2
            if nums[mid]==target:   # When we found the target, we are iterating left and right in order to find
                left=right=mid      # its leftmost and rightmost position by these while loops.
                while (left!=0 and nums[left-1]==target):left-=1
                while(right!=len(nums)-1 and nums[right+1]==target):right+=1
                return [left,right]
            if nums[mid]<target:left=mid+1
            else:right=mid-1
        return [-1,-1]       # If binary search cannot find target, it means that target is not in the list.
            


   # Binary Search Time Complexity O(logn)
