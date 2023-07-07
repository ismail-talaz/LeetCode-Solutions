class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        num=start=0
        total=sum(arr[:k])
        if total/k>=threshold:num+=1

        for end in range(k,len(arr)):
            total+=arr[end]-arr[start]
            if total/k>=threshold:num+=1
            start+=1
        
        return num