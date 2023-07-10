class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashTable={}
        minimum=float('inf')
        for i in range(len(cards)):
            if cards[i] in hashTable:
                minimum=min(i-hashTable[cards[i]]+1,minimum)
            hashTable[cards[i]]=i
        if minimum==float('inf'):return -1
        else: return minimum
