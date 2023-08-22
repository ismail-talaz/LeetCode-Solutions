class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maximumSubarray(arr,low,high):
            if low==high:                                  # By Divide and Conquer Algorithm
                return arr[low]                            # Time Complexity Big Theta θ(nlogn)
            else:
                mid=(low+high)//2
                left=maximumSubarray(arr,low,mid)
                right=maximumSubarray(arr,mid+1,high)
                cross=findMaxCrossing(arr,low,mid,high)

                return max(cross,max(left,right))

        def findMaxCrossing(arr,low,mid,high):
            leftmost=rightmost=mid
            leftsum=float('-inf')
            sum=0
            for i in range(mid,low-1,-1):
                sum+=arr[i]
                if sum>leftsum:
                    leftsum=sum
            rightsum=float('-inf')
            sum=0
            for i in range(mid,high+1):
                sum+=arr[i]
                if sum>rightsum:
                    rightsum=sum
            return max(leftsum,rightsum,leftsum+rightsum-arr[mid])
        
        return maximumSubarray(nums,0,len(nums)-1)
