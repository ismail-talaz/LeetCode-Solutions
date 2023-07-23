class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
      
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,None)
        dummy.next=head
        prev=dummy
        curr=head
        while (curr and curr.next):   # Traversing linked list

            if (curr.val<=curr.next.val):   # If next node is bigger than current node. It is okay, continue with next node.
                prev=curr
                curr=curr.next
            else:            # If next node is smaller than current node. It means that its position is wrong, delete it and insert from the beginning.
                temp=curr.next
                curr.next=curr.next.next   # This line deletes current node which locates in wrong position.

                secprev=dummy                          
                seccurr=dummy.next           # seccurr : second current,  secprev : second previous. To traverse linked list from the beginning.

                while(seccurr and seccurr.val<temp.val):   
                    secprev=seccurr                       # Find its correct position and insert it.
                    seccurr=seccurr.next
                secprev.next=temp
                temp.next=seccurr
        return dummy.next
