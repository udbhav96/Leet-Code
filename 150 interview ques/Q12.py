"""https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = s.split()[-1]
        a = len(word)
        return a
    
'''New Feature: Learned about the `split` method in Python, 
which is used to convert a string into a list by splitting 
it based on a specified delimiter (default is whitespace).
'''