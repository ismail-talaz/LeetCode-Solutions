class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder=sum(nums)%p
        if not remainder:return 0
        mydict={0:-1}
        curr=0
        res=len(nums)
        for i,num in enumerate(nums):
            curr=(curr+num)%p
            if (curr-remainder)%p in mydict:
                res=min(res,i-mydict[(curr-remainder)%p])
            mydict[curr]=i
        
        if res<len(nums):return res
        else:return -1
