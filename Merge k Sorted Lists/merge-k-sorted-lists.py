class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
      
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap=[]
        
        for i,ll in enumerate(lists):
            if ll:
                heapq.heappush(minHeap,(ll.val,i))
                lists[i]=lists[i].next

        dummy=ListNode(0)
        curr=dummy                                    # The running time is O(nlogk) which n is total number of nodes and k is the number of linked lists.
                                                      # The pop and insertion process costs O(logk) for each node. This process are executed by n timnes. Thus, time complexity is O(nlogk).
        while minHeap:

            val,index=heapq.heappop(minHeap)

            curr.next=ListNode(val)
            curr=curr.next

            
            if lists[index]:
                heapq.heappush(minHeap,(lists[index].val,index))
                lists[index]=lists[index].next
                
        return dummy.next
