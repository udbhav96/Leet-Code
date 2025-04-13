 /*https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=study-plan-v2&envId=top-interview-150*/
 #include <stddef.h>
//Try 1( 30 min)
struct ListNode {
    int val;
    struct ListNode *next;
  };
 
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    int count = 0;
    struct ListNode* current = head;

    while (current != NULL) {
        count++;
        current = current->next;
    }

    int target = count - n;

    if (target == 0) {
        struct ListNode* newHead = head->next;
        free(head);
        return newHead;
    }

    current = head;
    for (int i = 0; i < target - 1; i++) {
        current = current->next;
    }

    struct ListNode* toDelete = current->next;
    current->next = current->next->next;
    free(toDelete);

    return head;
}
//Hahahaha simple for me 
