"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
"""
nums = [3,4,5,6,7,3,8,7]
class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        for c in range(len(nums) - 1):
            if nums[c] != nums[c + 1]:
               nums[k] = nums[c]
               k += 1
        nums[k] = nums[-1]  
        k += 1
        return k 
print(removeDuplicates(nums))
    