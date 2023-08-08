class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while (curr and curr.next):
            newNode=ListNode(math.gcd(curr.val,curr.next.val),None)
            next=curr.next
            newNode.next=curr.next
            curr.next=newNode

            curr=next
          
        return head
