class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen=0
        mySet=set(nums)

        for num in mySet:
            
            currlen=1
            if num-1 not in mySet:    # It is the beginning of the sequence
                curr=num
                while curr+1 in mySet:
                    curr+=1
                    currlen+=1

            maxlen=max(maxlen,currlen)
        
        return maxlen
