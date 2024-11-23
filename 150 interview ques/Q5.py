"""
https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
"""

class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        a = 0 
        nums.sort()
        count = 1 
        if len(nums) == 1:
             a = nums[0]

        for i in range(1, len(nums)): 

            
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            
            if count > n / 2:
             a = nums[i]  

            
        return a    
            
            
        