'''https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1 (1.5hr)
height = [1,8,6,2,5,4,8,3,7]
i = 0 
j = len(height) -1 
v = 0 
while i < j:

    if height[i] < height[i + 1]:  
        i += 1  
    if height[j - 1] >  height[j]:  
        j -= 1
    else: 
        v = (j-i)**2
        break

    
'''This kind correct but not taking the case of  i = j '''
#Try 2 (Seen) Optimize too  (30 min)
class Solution:
    def maxArea(self, height) :
        n = len(height)
        i, j, ans = 0, n - 1, 0
        while i < j:
            ans = max(ans, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans

  