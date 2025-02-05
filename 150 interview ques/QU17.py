'''https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150'''
nums = [0]
g = len(nums) -1 

b = 0
if g  == nums[-1] and g != 0 :
    print(2)
if g < nums[-1]:
    print(1)
if g > nums[-1]: 
    while g >= 0:
        if nums[g] == 0:
            print(0)
        b += 1
        g -= nums[g]  
print(b)
