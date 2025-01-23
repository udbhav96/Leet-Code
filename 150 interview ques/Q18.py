'''https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1(2hr 34min) 
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        prevSuffix = 1
        for i in range(n - 2, -1, -1):
            prevSuffix *= nums[i + 1]
            ans[i] *= prevSuffix

        return ans

'''I learn the selection sorting alogorithm'''