/*https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150*/
#include<stdio.h>
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i, j;
    for (i = 0; i < numsSize; i++) {
        for (j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                int* result = (int*)malloc(2 * sizeof(int)); // Allocate memory
                result[0] = i;
                result[1] = j;
                *returnSize = 2; // Set return size
                return result;
            }
        }
    }
    *returnSize = 0; // No result found
    return NULL;
}
