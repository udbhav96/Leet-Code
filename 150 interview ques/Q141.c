/*https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150*/
#include <stdio.h>
#include <stdbool.h>  // ✅ Include this for bool

// Definition for singly-linked list
struct ListNode {
    int val;
    struct ListNode *next;
};

bool hasCycle(struct ListNode *head) {
    if (!head || !head->next) {
        return false;
    }

    struct ListNode* slow = head;
    struct ListNode* fast = head;

    while (fast && fast->next) {
        slow = slow->next;         // Move slow by 1 step
        fast = fast->next->next;   // Move fast by 2 steps

        if (slow == fast) {        // If they meet, cycle detected
            return true;
        }
    }
    return false;  // If loop exits, no cycle
}

