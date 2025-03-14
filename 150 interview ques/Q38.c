/*https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150*/
#include <stdlib.h>  

//Try 1(40 Min)
struct ListNode {
     int val;
     struct ListNode *next;
};
 
// struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
//     if (list1 == NULL) {
//         return list2;
//     }
//     if (list2 == NULL) {
//         return list1;
//     }
//     struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
//     struct ListNode* tail = dummy;
//     while (list1 != NULL && list2 != NULL) {
//         if (list1->val > list2->val) {
//             tail->next = list2;  // Attach the smaller node
//             list2 = list2->next;
//         } else if (list2->val > list1->val) {
//             tail->next = list1;
//             list1 = list1->next;
//         } else {  // Both are equal
//             tail->next = list2;
//             list2 = list2->next;
//             tail = tail->next;
            
//             tail->next = list1;
//             list1 = list1->next;
//         }
//         if(list1 == NULL){
//             if(list2->next->val > list2->val){
//                 tail->next = list2;
//                 list2 = list2->next;
//             }else if(list2->next->val < list2->val){
//                 tail->next = list2->next;
//                 list2 = list2->next->next; 
//             }else{
//                 tail->next = list2;
//                 list2 = list2->next;
//                 tail = tail->next;
                
//                 tail->next = list2->next;
//                 list2 = list2->next->next; 

//             }
//         if(list2 == NULL){
//             if(list1->next->val > list1->val){
//                 tail->next = list1;
//                 list1 = list1->next;
//             }else if(list1->next->val < list1->val){
//                 tail->next = list1->next;
//                 list1 = list1->next->next; 
//             }else{
//                 tail->next = list1;
//                 list1 = list1->next;
//                 tail = tail->next;
                
//                 tail->next = list1->next;
//                 list1 = list1->next->next; 

//             }
//         }
//         tail = tail->next;  // Move tail forward
//     }
//     return dummy->next;
//   }

/*Code is correct i used unusual condition */

//Try 2 (30min)
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (list1 == NULL) {
        return list2;
    }
    if (list2 == NULL) {
        return list1;
    }
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* tail = dummy;
    while (list1 != NULL && list2 != NULL) {
        if (list1->val > list2->val) {
            tail->next = list2;  // Attach the smaller node
            list2 = list2->next;
        } else if (list2->val > list1->val) {
            tail->next = list1;
            list1 = list1->next;
        } else {  // Both are equal
            tail->next = list2;
            list2 = list2->next;
            tail = tail->next;
            
            tail->next = list1;
            list1 = list1->next;
        }
        tail = tail->next;  // Move tail forward
    }
    if (list1 != NULL) {
        tail->next = list1;
    } else {
        tail->next = list2;
    }

    return dummy->next;
  }





        
