class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mySet=set()
        curr=head
        while (curr):                                         # Time Complexity O(N)
            if curr not in mySet:mySet.add(curr)              # Space Complexity O(N)
            else:return True
            curr=curr.next
        return False
