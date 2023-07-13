class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1

        while (left<=right):
                                                          # Binary Search Solution              
            mid=(left+right)//2                           # O(logn) Time Complexity

            if target==nums[mid]:
                return mid
            
            if nums[left]>nums[mid]:
                if target<nums[left] and target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
            elif nums[right]<nums[mid]:
                if target<nums[mid] and target>nums[right]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
