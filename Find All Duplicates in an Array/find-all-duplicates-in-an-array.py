class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashT={}
        result=[]
        for num in nums:
            if num in hashT:result.append(num)
            else:hashT[num]=1
        return result
