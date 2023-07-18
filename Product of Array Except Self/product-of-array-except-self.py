class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp=1
        result=[1]

        for i in range(1,len(nums)):
            result.append(1)
            result[i]=result[i-1]*nums[i-1]
            

        for i in range(len(nums)-1,-1,-1):
            result[i]*=temp
            temp*=nums[i]

        return result 
