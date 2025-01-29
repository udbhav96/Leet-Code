'''https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1 ( 20 min)
strs = ["flower","flow","flight"]
i = 0 
a = []
while i < len(strs):
    j = i + 1 
    k = len(strs) - 1
    while j < k:
        if strs[i][i] == strs[j][i] == strs[k][i]:
            a.append(strs[i][i])
            j += 1
            k -= 1
    i += 1
    
print(a)
'''Too many error i am not going tell find yourself'''
#Try 2 ( 20 min )
strs = ["flower","flow","flight"]
i = 0 
j = 0 
k = 0 
a = []
while i < len(strs)- 2 :
    j = i + 1 
    k = len(strs) -  1 - i
    z = 0 
    while j < k and k > 0:
        if strs[i][z] == strs[j][z] == strs[k][z]:
            a.append(strs[i][z])
            z += 1
        j += 1 
        k += 1
    i += 1

'''Error  z is iterated all the way and not stoping , plz z stop '''
#Try 3 Final and optimized code ( 45 min )
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a = []
        z = 0  

        while z < len(strs[0]):  
            char = strs[0][z]  
            for word in strs:  
                if z >= len(word) or word[z] != char:  
                    return "".join(a)  
            a.append(char)
            z += 1  

        result = ""
        for char in a:
            result += char  

        return result
#Good solution 
class Solution:
    def longestCommonPrefix(self, strs: str[str]) -> str:
        if not strs:
            return ""
        new = ""
        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                new += first[i]
            else:
                break
        return new

    
