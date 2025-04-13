"""
https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&envId=top-interview-150
"""
#Try 1 
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        dl = [int(digit) for digit in str(x)]
        for j in range(len(dl) // 2):
            if dl[j] != dl[-(j + 1)]:
                return False
        return True