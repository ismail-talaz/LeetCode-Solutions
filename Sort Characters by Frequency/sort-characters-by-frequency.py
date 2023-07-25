class Solution:
    def frequencySort(self, s: str) -> str:
        mydict={}
        res=""
        
        for char in s:
            if char in mydict:mydict[char]+=1 
            else:mydict[char]=1
        
        for item in sorted(mydict.items(), key=lambda item: item[1], reverse=True):
            res+=item[0]*item[1]
        return res
