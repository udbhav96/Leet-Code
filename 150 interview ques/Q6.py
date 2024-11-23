"""
https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = rotated[i]

   


