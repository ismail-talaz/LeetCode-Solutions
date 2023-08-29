class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left, right = i+1, len(numbers)-1
            res = target - numbers[i]
            while (left <= right):
                mid = (left+right)//2             # Time Complexity O(nlogn)
                if numbers[mid] == res:           # Space Complexity O(1)
                    return [i+1, mid+1]
                elif numbers[mid] < res:
                    left = mid+1
                else:
                    right = mid-1
