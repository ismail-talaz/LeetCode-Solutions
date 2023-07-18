class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr=best=0

        for alt in gain:
            curr+=alt
            best=max(curr,best)
        
        return best
