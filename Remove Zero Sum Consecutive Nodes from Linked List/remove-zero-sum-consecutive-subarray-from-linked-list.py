class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        lol = ListNode(0,head)
        prefix=0
        hashT={0:lol}
        curr=head
        while curr:
            prefix+=curr.val
            hashT[prefix]=curr
            curr=curr.next
        
        prefix=0                                     # HASH TABLE O(n) Time Complexity
        curr=lol

        while curr:
            prefix+=curr.val
            curr.next=hashT[prefix].next
            curr=curr.next
        return lol.next