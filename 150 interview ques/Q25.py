'''https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1 (40)
s = "0P"
lc = ""
r = ""
for i in s:
    if 'A' <= i <= 'Z':
        lc = i
        for j in range(26):
            if i == chr(65+j):
                lc = chr(97 + j)
        r += lc
    else:
        r += i

a = []
for i in r:
    if 'a' <= i  <= 'z' :
        a.append(i)
print(a)
b = a[:]


for i in range(len(s)//2):
    a[i] , a[-(i+1)] = a[-(i+1)] , a[i]

if a == b:
    print(True)
else: 
    print(False)
'''Error : i used the swaping which is not  same as reversed '''
#Try 2 Final (50 min)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lc = ""
        r = ""
        for i in s:
           if 'A' <= i <= 'Z':
            lc = i
            for j in range(26):
             if i == chr(65+j):
              lc = chr(97 + j)
              r += lc
           elif 'a' <= i <= 'z' or '0' <= i <= '9':
              r += i
        return r == r[::-1]
'''Oki i had done it , and wasted my 1'''
#Optamize Code
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1

            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1

        return True