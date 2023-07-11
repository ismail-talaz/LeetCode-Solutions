class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=total=0
        minimum = float('inf')
        length=len(nums)
        for end in range(length):
            total+=nums[end]
            while (total>=target):                         # Sliding Window Technique with O(n) Time Complexity
                minimum=min(end-start+1,minimum)
                total-=nums[start]
                start+=1
        
        if minimum==float('inf'): return 0
        else: return minimum
