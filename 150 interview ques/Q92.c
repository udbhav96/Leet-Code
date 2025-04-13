/*https://leetcode.com/problems/reverse-linked-list-ii/submissions/1600517043/?envType=study-plan-v2&envId=top-interview-150*/
#include <stddef.h>
struct ListNode {
    int val;
    struct ListNode *next;
  };
//Try 1 (Seen little bit)
  struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    if (head == NULL || left == right) return head;

    struct ListNode dummy;
    dummy.next = head;
    struct ListNode* prev = &dummy;

    for (int i = 1; i < left; i++) {
        prev = prev->next;
    }

    struct ListNode* curr = prev->next;
    struct ListNode* nextNode = NULL;

    for (int i = 0; i < right - left; i++) {
        nextNode = curr->next;
        curr->next = nextNode->next;
        nextNode->next = prev->next;
        prev->next = nextNode;
    }

    return dummy.next;
}
//saw how to revers a link list and how the cut and connect work its like a puzzle for me 