class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSoFar=total=sum(nums[:k])
        start=0                                       # The code starts for loop at the k'th element because we do not have to add up the numbers until k'th element.  
        for i in range(k,len(nums)):                  # In this way, the time complexity of the algorithm has been decreased a little bit.
            total+=nums[i]-nums[start]                # Sliding Window Technique. We iterate the subarray by increasing end point and start point at the same time. 
            maxSoFar=max(total,maxSoFar)              # At the end of the for loop, maximum summation of subarrays of length k will be found.
            start+=1
        return maxSoFar/k
