class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hashT={}
        for num in nums:
            if num in hashT:return num
            else:hashT[num]=1
