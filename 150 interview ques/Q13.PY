'''https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150'''
#try 1
neddle = "code"
haystack = "leetcode"
a =  0
for i  in range(len(neddle)):
   if  haystack[i] == neddle[i] : 
    a = 0
   else : 
    a = -1
print(a)
#try 2
haystack = "hello"
needle = "ll"
a = 0
b = 0
for i in range(len(haystack)):
    if haystack[i] == needle[0]:
        a = i
        for j in range(len(needle)):
            if haystack[a] == needle[j]:
                a += 1
                b = i
            else:
                b = -1
                break
    if b != -1:
        break

print(b)
    
'''Work but less efficient and i got an second idea why not i slice it'''
#try 3
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a =0
        if len(haystack) < len(needle):
            return -1 
        for i in range(len(haystack)- len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
            else:
                a = -1 
        return a
'''Optimaum code fr easy '''








