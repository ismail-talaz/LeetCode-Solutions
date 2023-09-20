class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen=0
        mySet=set(nums)
        visited=set()

        for num in nums:
            currlen=1
            curr=num
            if num in visited:continue
            visited.add(curr)

            while curr-1 in mySet:
                curr-=1
                currlen+=1
                visited.add(curr)
            
            curr=num
            while curr+1 in mySet:
                curr+=1
                currlen+=1
                visited.add(curr)
            
            maxlen=max(maxlen,currlen)
        
        return maxlen
