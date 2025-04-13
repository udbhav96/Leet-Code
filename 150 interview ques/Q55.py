'''https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1 (1 hr 33 min ) 
nums = []
i = 0
if len(nums) == 1:
  i = True
else : 
    while i < len(nums) :
     i = nums[0]
     
     if i >= len(nums):  
      i = True
      break
     elif nums[i] == 0 and len(nums) > 1:
      i = False
      break  
     i = i + nums[i]  
print(i)
"This code isn't well-written, and I'll comment on it after reviewing it. If you continue with this approach, you're likely to encounter multiple runtime errors. The issue comes from introducing unnecessary variables. After sorting through 5 or 6 cases (which will likely fail), you'll encounter something like this, and eventually, you'll face a 'Time Exceeded' error, which proves that this approach is inefficient. Another major problem is that 'i' starts as an integer and is later changed to a boolean, which is poor practice. You should rethink your approach and try again.Just Fuck this code and try again"
#try 2 (2 hr + 3-4 youtube tutorials)
class Solution(object):
    def canJump(self, nums):
        g = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= g:
                g = i
        return g == 0
'''---> Objective:
Determine if you can reach the last index of an array starting from the first index, given each element in the array represents your maximum jump length at that position.

---> Approach:

Greedy Algorithm:
Start from the last index (goal = len(nums) - 1).
Traverse the array backwards:
If the current index can jump to or beyond the goal, update the goal to the current index.
If the goal is reduced to 0, return True; otherwise, return False'''





