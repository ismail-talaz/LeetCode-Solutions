class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
                                                                      # Floyd’s Cycle Finding Algorithm [Two Pointers]
        while (slow!=None and fast!=None and fast.next!=None):        # Time Complexity O(N)
            slow=slow.next                                            # Space Complexity O(1)
            fast=fast.next.next
            if (slow==fast):
                slow=head
                while (slow!=fast):
                    slow,fast=slow.next,fast.next
                return slow
        
        return None
