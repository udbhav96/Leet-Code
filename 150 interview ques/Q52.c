/*https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=top-interview-150*/
/*
  🧠 How XOR Helps Find the Unique Number

  Problem:
  - You're given an array where every number appears twice except for one.
  - You need to find that one unique number.

  ✅ XOR ( ^ ) — The Trick:
  - A ^ A = 0        → Same numbers cancel out
  - A ^ 0 = A        → XOR with 0 gives the number itself
  - XOR is commutative & associative → Order doesn't matter

  So if we XOR all numbers:
  - The ones that appear twice will cancel out.
  - Only the unique number will remain.

  Example: [4, 1, 2, 1, 2]

  Step-by-step:
  result = 0
  result ^= 4 → 0 ^ 4 = 4
  result ^= 1 → 4 ^ 1 = 5
  result ^= 2 → 5 ^ 2 = 7
  result ^= 1 → 7 ^ 1 = 6
  result ^= 2 → 6 ^ 2 = 4

  Final result = 4 (which is the unique number)

  💡 Efficient:
  - Time Complexity: O(n)
  - Space Complexity: O(1)
  - No need for extra memory like hash tables or arrays
*/

/* ✅ Final C code: Seen */

int singleNumber(int* nums, int numsSize) {
    int result = 0;
    for(int i = 0; i < numsSize; i++) {
        result ^= nums[i];  
    }
    return result;  
}
