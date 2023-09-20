class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:                         # Time Complexity O(n)
        maxlen=0                                                                  # Space Complexity O(n)
        mySet=set(nums)

        for num in mySet: # Iterating through set is better than array because it deletes the duplicates.
            
            currlen=1
            if num-1 not in mySet:    # It is the beginning of the sequence
                curr=num
                while curr+1 in mySet:
                    curr+=1
                    currlen+=1

            maxlen=max(maxlen,currlen)
        
        return maxlen
