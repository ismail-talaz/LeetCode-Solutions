class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        dict={}
        result=[]
        for num in nums1:
            dict[num]=[1]
        for num in nums2:
            if num in dict and 2 not in dict[num]:dict[num].append(2)
            elif num not in dict:dict[num]=[2]
        for num in nums3:
            if num in dict and 3 not in dict[num]:dict[num].append(3)
            elif num not in dict:dict[num]=[3]
        for key in dict:
            if len(dict[key])>1:result.append(key)
            
        return result
