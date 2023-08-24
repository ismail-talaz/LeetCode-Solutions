class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mySet=set()
        while (head):
            if head in mySet:return head                        # Time Complexity O(N)
            else:                                               # Space Complexity O(N)
                mySet.add(head)
                head=head.next
        return None
