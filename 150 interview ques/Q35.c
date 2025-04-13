/*https://leetcode.com/problems/search-insert-position/submissions/1573815316/?envType=study-plan-v2&envId=top-interview-150*/
//Try 1 (20min)
int searchInsert(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return mid; // Found target
        }

        if (nums[mid] < target) {
            left = mid + 1; // Search right half
        } else {
            right = mid - 1; // Search left half
        }
    }

    return left; // Correct insert position
}
