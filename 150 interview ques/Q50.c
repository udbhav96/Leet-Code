/*https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150*/
#include <stddef.h>
struct ListNode {
    int val;
    struct ListNode *next;
  };
  struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode dummy;
    dummy.next = head;

    struct ListNode* prev = &dummy;

    while (head != NULL) {
        if (head->next != NULL && head->val == head->next->val) {
            int dupVal = head->val;

            while (head != NULL && head->val == dupVal) {
                struct ListNode* temp = head;
                head = head->next;
                free(temp);
            }

            prev->next = head;
        } else {
            prev = head;
            head = head->next;
        }
    }

    return dummy.next;
}
