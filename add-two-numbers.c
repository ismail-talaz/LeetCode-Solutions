#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *head=NULL;
    struct ListNode *curr1=NULL,*curr2=NULL,*new=NULL,*prev=NULL;
    int carry=0,val1,val2,s=0;
    prev=head;
    curr1=l1;
    curr2=l2;
    
    while (curr1 || curr2 || carry) {
        val1=curr1?curr1->val:0;
        val2=curr2?curr2->val:0;

        new=malloc(sizeof(struct ListNode));
        new->next=NULL;
        if (s==0) head=new;


        if (val1+val2+carry>=10) {
            new->val=(val1+val2+carry)%10;
            carry=1;  
        }
        else {
            new->val=(val1+val2+carry);
            carry=0;
        }

        if (prev) prev->next=new;
        prev=new;

        if (curr1) curr1=curr1->next;
        if (curr2) curr2=curr2->next;
        s++;
    }

    return head;
}
