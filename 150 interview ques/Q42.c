/*https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=study-plan-v2&envId=top-interview-150*/
//Try 1 (20 min)

int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int* arr = (int*)malloc(2 * sizeof(int));  // ✅ Allocating memory on the heap
    arr[0] = -1;
    arr[1] = -1; // Default values if target is not found

    int left = 0;
    int right = numsSize - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            arr[0] = mid;
            arr[1] = mid;  // Start with mid for both

            // Expand left to find the first occurrence
            while (arr[0] > 0 && nums[arr[0] - 1] == target) {
                arr[0]--;
            }

            // Expand right to find the last occurrence
            while (arr[1] < numsSize - 1 && nums[arr[1] + 1] == target) {
                arr[1]++;
            }

            *returnSize = 2; // Set returnSize to 2
            return arr;
        }

        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    *returnSize = 2;
    return arr;
}
