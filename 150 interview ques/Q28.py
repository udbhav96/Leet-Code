'''https://leetcode.com/problems/factorial-trailing-zeroes/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1 ( 40min )
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        k = 1
        for i in range(n):
           if n == 0:
             return 1
           k *= (n-i)
        c = str(k)

        a = 0
        for  i in range(len(c)-1 , -1 , -1):
          if c[i] == "0":
            a += 1
          else: 
            return a
'''Its easy but not optimum'''
#Optimize Code
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res
# This code calculates the number of trailing zeroes in the factorial of n.
# Trailing zeroes are created by factors of 10, and since 10 is the product of 2 and 5,
# the number of trailing zeroes is determined by the number of times 5 is a factor in the numbers 
# from 1 to n (since there are always more factors of 2 than 5 in a factorial).
#
# The algorithm works by repeatedly dividing n by 5 to count:
# 1. Multiples of 5 (such as 5, 10, 15, 20, etc.).
# 2. Higher powers of 5 (like 25, 125, etc.), which contribute additional factors of 5.
#
# The sum of these counts gives the total number of trailing zeroes in n!.
# The loop stops when n becomes less than 5, as higher powers of 5 no longer contribute.
#
# This approach is efficient with a time complexity of O(log₅(n)), making it much faster
# than directly calculating the factorial of n.
