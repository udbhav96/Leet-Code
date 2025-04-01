/*https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150*/
//Try 1
int search(int* nums, int numsSize, int target) {
    int j ;
    for( j = 0 ; j < numsSize - 1 ; j++){
        if(nums[j] > nums[j+1]){
            break;
        }
    }
    if(nums[j] == target){
        return j;
    }
    int left = 0;
    int right = numsSize - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
       
        if (nums[j]< target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return left;

    
    
}
//Try 2 
#include <stdio.h>

int search(int* nums, int numsSize, int target) {
    int left = 0, right = numsSize - 1;
    
    // Find the pivot (smallest element index)
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] > nums[right]) { // Pivot is in the right half
            left = mid + 1;
        } else { // Pivot is in the left half
            right = mid;
        }
    }
    
    int pivot = left;
    left = 0, right = numsSize - 1;
    
    // Determine which half to search
    if (target >= nums[pivot] && target <= nums[right]) {
        left = pivot;
    } else {
        right = pivot - 1;
    }
    
    // Standard Binary Search
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

