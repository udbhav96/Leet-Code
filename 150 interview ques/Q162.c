/*https://leetcode.com/problems/find-peak-element/submissions/1573841725/?envType=study-plan-v2&envId=top-interview-150*/
//Try 1 (20min)
int findPeakElement(int* nums, int numsSize) {
    int left = 0;
    int right = numsSize - 1;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (nums[mid] > nums[mid + 1]) {
            // Peak is in the left half
            right = mid;
        } else {
            // Peak is in the right half
            left = mid + 1;
        }
    }
    
    return left;  
}
