class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i=1
        dummy=ListNode(None)
        dummy.next=head
        prev,curr=dummy,head

        while (i<left):
            prev=curr
            curr=curr.next
            i+=1
        
        while (i<right):
            next=curr.next
            curr.next=next.next
            next.next=prev.next
            prev.next=next
            i+=1
        
        return dummy.next
