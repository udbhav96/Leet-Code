/*https://leetcode.com/problems/single-number-ii/?envType=study-plan-v2&envId=top-interview-150*/
//Try 1 ( 30 min)

int singleNumber(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) {
        int found = 0;
        for (int j = 0; j < numsSize; j++) {
            if (nums[i] == nums[j] && i != j) {
                found = 1;
                break;
            }
        }
        if (!found) {
            return nums[i];
        }
    }
    return -1;
}
//Uses Brute gorce not good tho 
//Optimize code 
int singleNumber(int* nums, int numsSize) {
    int one=0,multi=0;
    for(int i=0;i<numsSize;i++){
        one = (one^nums[i]) & ~multi;
        multi=(multi^nums[i]) & ~one;
    }
    return one;
}
/*
    Step-by-step explanation of this line:

    one = (one ^ nums[i]) & ~multi;

    1. (one ^ nums[i])
       - This toggles the bits of nums[i] in 'one'.
       - If a bit is not in 'one', it gets added (seen once).
       - If it's already in 'one', it gets removed (seen twice).

    2. & ~multi
       - This removes any bits from 'one' that are already in 'multi'.
       - Ensures bits that have appeared twice (in 'multi') don't stay in 'one'.

    Overall:
    - 'one' tracks bits that have appeared exactly once so far.
    - Once a bit has been seen three times, it gets removed from both 'one' and 'multi'.
*/
