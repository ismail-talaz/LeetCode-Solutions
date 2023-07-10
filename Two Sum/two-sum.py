class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        hashTable={}

        for i in range(length):
            hashTable[nums[i]]=i          # Hash table is created and filled.

        for i in range(length):
            complement=target-nums[i]
            if (complement in hashTable and i!=hashTable[complement]):      # In every loop, we look for whether the complement of the current value is in the hash table.
                return [i,hashTable[complement]]
        return []                    # After the all loops, if there is no complement of the every values, we return empty list.
