"""
https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
"""
class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for c in range(len(nums)):
            if nums[c] != val:
                nums[k] = nums[c]
                k += 1
        return k
