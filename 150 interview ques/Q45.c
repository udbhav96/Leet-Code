/*https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=study-plan-v2&envId=top-interview-150*/
//Try 1 Final ( 3hr)
void mergeSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size, int* merged) {
    int i = 0, j = 0, k = 0;

    while (i < nums1Size && j < nums2Size) {
        if (nums1[i] < nums2[j]) merged[k++] = nums1[i++];
        else merged[k++] = nums2[j++];
    }

    while (i < nums1Size) merged[k++] = nums1[i++];
    while (j < nums2Size) merged[k++] = nums2[j++];
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int mergedSize = nums1Size + nums2Size;
    int* merged = (int*)malloc(mergedSize * sizeof(int));
    
    mergeSortedArrays(nums1, nums1Size, nums2, nums2Size, merged);

    
    for (int i = 0; i < mergedSize; i++) {
        printf("%d ", merged[i]);
    }
    printf("\n");

    double median;
    if (mergedSize % 2 == 0) {
        median = (merged[mergedSize / 2 - 1] + merged[mergedSize / 2]) / 2.0;
    } else {
        median = merged[mergedSize / 2];
    }

    free(merged); 
    return median;
}
//I had learn merge sort again idk why i kept forgoting it i had solved this in  multile  try but i forgot to saved them  and  this is not the optimize code tho  i will put optimal code later there are some easy optimal code as they are taking more memory so  i will final a code which take low memory and optimal later 