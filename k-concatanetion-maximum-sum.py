class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        def kadanealgo(arr):
            currSum=0
            maxSum=0
            for i in range(len(arr)):
                currSum=max(arr[i],currSum+arr[i])
                maxSum=max(currSum,maxSum)
        
            return maxSum

        if k==1:
            return kadanealgo(arr)

        summ=sum(arr)
        
        if summ>0:
            return (((k-2)*summ)+kadanealgo(arr+arr))%(10**9 + 7)
        else: 
            return kadanealgo(arr+arr)%(10**9 + 7)   