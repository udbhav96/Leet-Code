'''https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1(Seen)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pair = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in "({[":  
                stack.append(char)
            elif char in ")}]":  
                if not stack or stack[-1] != pair[char]:
                    return False  
                stack.pop() 

        return len(stack) == 0
'''I had code seen it because idk about stack'''