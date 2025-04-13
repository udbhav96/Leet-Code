"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
"""

#Final code (seen): Time Taken(2hr 46min)
class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
"""Concept Learn : Kadane's Algorithm
Kadane's Algorithm is a dynamic programming technique used to find the maximum subarray sum in an array of numbers. The algorithm maintains two variables: max_current represents the maximum sum ending at the current position, and max_global represents the maximum subarray sum encountered so far. At each iteration, it updates max_current to include the current element or start a new subarray if the current element is larger than the accumulated sum. The max_global is updated if max_current surpasses its value"""   

#1st try 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        m = prices.index(min(prices))
        if m == prices.index(prices[-1]): 
            d = prices[:m]
            e = d.index(min(d))
            f = d[e:]
            g = f.index(max(f)) + e 
            c = prices[g]-prices[e]
        else: 
            a = prices[m:]
            b = a.index(max(a)) + m
            c = prices[b]-prices[m]

        return c
'''This code attempts to find the minimum price and then calculate the profit by finding
 the maximum price after the minimum. However, it fails to handle cases where the 
 minimum price is at the end of the list or other edge cases. As a result, it passes 151 
 test cases, but it doesn't fully solve the problem, leading to incorrect results for some scenarios.'''

#2nd try 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 2:
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
        else:
            for i in range(1, len(prices) - 1):
                if prices[i - 1] > prices[i] < prices[i + 1]:
                    a = prices[i:]
                    b = a.index(max(a)) + i
                    c = prices[b] - prices[i]
                    return c
        return 0

'''This code only handles the case where the local minimum is in the middle of the list.
 It doesn't consider cases where the minimum price is at the start or end of the list,
 which is why it fails in those scenarios. This leads to a flawed solution and makes
 the code unnecessarily complex with nested if-else statements.'''
