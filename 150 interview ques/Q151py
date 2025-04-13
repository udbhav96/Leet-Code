'''https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1 Final (1hr 35 min)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = []
        k = ""
        for i in s:
           if i != " ":
             k += i
           if i == " " and k :
             a.append(k)
             k = ""      
        if k: 
         a.append(k)
         k =""
        for i in range(len(a)//2):
          a[i] , a[-(i+1)] = a[-(i+1)] , a[i]
        for i in range(len(a)):
          k += a[i]
          if i != len(a)-1:
            k += " "
        return k 
'''Things i Leared  , how to convert string into list then swap then append the element of list in the single string'''