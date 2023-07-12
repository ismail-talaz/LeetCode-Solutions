class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myDict={}
        result=[]
        for i in range(len(nums1)):
            if not nums1[i] in myDict:
                myDict[nums1[i]]=1
        for i in range(len(nums2)):
            if nums2[i] in myDict and not nums2[i] in result:
                result.append(nums2[i])
        return result  
