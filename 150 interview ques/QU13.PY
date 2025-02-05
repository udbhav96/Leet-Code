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








