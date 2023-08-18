class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
  
        if not (head and head.next): return head                     # Time Complexity O(N)

        new = head.next
        head.next, new.next = self.swapPairs(head.next.next), head         # Recursive Approach

        return new
