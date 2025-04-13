/*https://leetcode.com/problems/rotate-list/?envType=study-plan-v2&envId=top-interview-150*/
#include <stddef.h>

struct ListNode {
    int val;
    struct ListNode *next;
};
//Try 1 (50 min)
struct ListNode* rotateRight(struct ListNode* head, int k) {
    int count = 0;
    struct ListNode* current = head;
    
    while (current != NULL) {
        count += 1;
        current = current->next;
    }
    k = k % count;
    int i = 0;
    while(i < k){
        struct ListNode* prev = NULL;
        struct ListNode* curr = head;
        while( curr != NULL){
            prev = curr;
            curr -> next;
        }
        prev -> next = NULL;
        curr -> next = head;
        curr = head;
      
    }
    return head;
 


    
}
//This code failed because i had use infinite loop
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (!head || !head->next || k == 0) return head;

    int len = 1;
    struct ListNode* tail = head;
    while (tail->next) {
        tail = tail->next;
        len++;
    }

    k = k % len;
    if (k == 0) return head;

    tail->next = head;

    struct ListNode* newTail = head;
    for (int i = 0; i < len - k - 1; i++) {
        newTail = newTail->next;
    }

    struct ListNode* newHead = newTail->next;
    newTail->next = NULL;

    return newHead;
}
