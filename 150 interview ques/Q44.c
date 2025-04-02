/*https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/?envType=study-plan-v2&envId=top-interview-150*/
//Try 1 (10 min)
int findMin(int* nums, int numsSize) {
    int left = 0, right = numsSize - 1;

    while (left < right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] > nums[right]) { // Pivot is in the right half
        left = mid + 1;
    } else { // Pivot is in the left half
        right = mid;
    }
}
int pivot = left;
return nums[pivot];

}
//Hahahaha... this is the part of Q43