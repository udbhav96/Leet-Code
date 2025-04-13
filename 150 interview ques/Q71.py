'''https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1 (Final) 2 hr
path = "/home/user//Documents/../Pictures"
a = []
j = 0
stack=[]
for i in range(len(path)):
    if path[i] == "/":
        a.append(path[j:i])  
        j = i + 1  

a.append(path[j:]) 
for i in a:
    if i == "." or i == "":
        continue
    elif i == "..":
        if stack:
            stack.pop()
    else:
        stack.append(i)
string = "/".join(stack)

print(string)
'''Make a list with the element then use stack pretty easy'''
#Optimum code
class Solution(object):
    def simplifyPath(self, path):
        stack = []
        directories = path.split("/")
        for dir in directories:
            if dir == "." or not dir:
                continue
            elif dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return "/" + "/".join(stack)
'''Same just uses in build function '''