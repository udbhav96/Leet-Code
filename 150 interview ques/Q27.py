'''https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1 ( 20 min)
s = "aaaaaa"
t = "bbaaaa"
i = 0 
j = 0
a = True
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        a = True
        i += 1
    else:
        j+= 1
        a = False
if len(t) == 0 and len(s) != 0:
            a = False
if i == len(s):
        
        print(a)
else :
      
      print(False)
'''Error : There was several error in the cases of the cod'''
#Try 2 Final (40 min)
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        i = 0 
        j = 0
        a = False
        while i < len(s) and j < len(t):

          if s[i] == t[j]:
           a = True
           i += 1
          
          j+= 1
           
        if len(t) == 0 and len(s) != 0:
            a = False
        if len(s) == 0:
            a = True
        if i == len(s):
           a = a
        else:
           a = False
        return a
'''It is not the optimize xode i had use too many if and else statement which is not good for code '''
#Optimize Code
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


   
