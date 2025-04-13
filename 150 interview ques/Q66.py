"""
https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        b = int("".join(map(str , digits)))
        c = b +1
        d = [int(digit) for digit in str(c)]
        return d
        