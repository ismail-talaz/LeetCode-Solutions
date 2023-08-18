class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i=0
        currNode=list1
        while (currNode):
            if i+1==a:
                nextNode=currNode.next
                currNode.next=list2
                currNode=nextNode
            elif i==b:
                tail=currNode.next
                break
            else:
                currNode=currNode.next
            i+=1
        
        currNode=list2
        while (currNode.next):
            currNode=currNode.next
        currNode.next=tail

        return list1
