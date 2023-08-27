class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr=None,head
        
        while (curr):
            if (curr.next and curr.val==curr.next.val):
                while (curr.next and curr.val==curr.next.val):              # Time Complexity O(N)
                    curr=curr.next                                          # Space complexity O(1)
                if (prev):prev.next=curr.next
                else:head=curr.next
                curr=curr.next
            else:
                prev=curr
                curr=curr.next
        
        return head
