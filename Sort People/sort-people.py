class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        myDict={}
        result=[]
        for i in range(len(names)):myDict[heights[i]]=names[i]
    
        for item in sorted(myDict.items(), key=lambda item: item[0], reverse=True):
            result.append(item[1])
        return result
