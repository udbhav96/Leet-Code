/*https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150*/
//TRY 1(1hr)
#include <stdio.h>

struct ListNode {
     int val;
      struct ListNode *next;
 };

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* node1 = l1;
    struct ListNode* node2 = l2;
    while(!l1 == NULL || !l2 == NULL){

    }



    
}
//TRY 2 (3hr)(SEEN)
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int carry =0;
    struct ListNode* head = NULL;
    struct ListNode* tail = NULL;

    while (l1 != NULL || l2 != NULL || carry) {
      int sum = carry;
      if (l1) sum += l1->val, l1 = l1->next;
      if (l2) sum += l2->val, l2 = l2->next;
    
    carry = sum / 10;
    
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = sum % 10;
    newNode->next = NULL;

    if (head == NULL) {  // Special case for the first node
        head = newNode;
        tail = newNode;
    } else {
        tail->next = newNode;
        tail = newNode;
    }
  }
  return head;

    
}