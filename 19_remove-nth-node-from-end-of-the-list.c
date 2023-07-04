#include <stdio.h>
#include <stdlib.h>


struct ListNode {
    int val;
    struct ListNode *next;
};
 
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode *curr=NULL,*prev=NULL;
    int i,size=1;

    curr=head;
    while (1) {
        if (curr->next!=NULL) {
            size++;                               /* So as to find out which node we will delete from the beginning, 
                                                    we need to measure the size of the linked list. This while loop continues until it reaches the tail node. */
            curr=curr->next;            
        }
        else break;
    }

    for (i=0,n=size-n,curr=head;curr;i++) {

        if (i==n) {
            if (prev) prev->next=curr->next;                   
            else head=curr->next;                 /* Here in for loop, we access the node and tie the previous and next nodes up.
                                                     After, we deallocate the memory of the deleted node. */
            free(curr);
            break;
        }
        prev=curr;
        curr=curr->next;
    }
    return head;
}