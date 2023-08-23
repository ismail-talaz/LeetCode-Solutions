class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        
        while (fast!=None and fast.next!=None):        # Time Complexity O(N)
            slow=slow.next                             # Space Complexity O(1)
            fast=fast.next.next
            if (slow==fast):return True
        return False
