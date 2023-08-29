class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left,right=0,len(numbers)-1
        while (left<right):                       # Time Complexity O(N)
            res=numbers[left]+numbers[right]      # Space Complexity O(1)
            if res>target:right-=1
            elif res<target:left+=1
            else:return [left+1,right+1]
