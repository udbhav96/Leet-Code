"""
https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&envId=top-interview-150
"""
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        dl = [int(digit) for digit in str(x)]
        for i in range(len(dl) // 2):
            if dl[i] != dl[-(i + 1)]:
                return False
        return True