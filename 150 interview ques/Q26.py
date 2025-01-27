'''https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150'''
nums = [2, 3, 1, 2, 4, 3]
i = 0
target = 7

while i < len(nums) - 1:  
    j = i + 1
    while j < len(nums):  
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        j += 1  
    i += 1

n = []
i = 0 
k = 0
while i < len(nums):

    k += nums[i]
    n.append(nums[i])
    target -= i
    if target < 0:
        k -= nums[i]
        n.pop()
        continue
    if i == target:
        print(1)
        break
    if target == 0:
        print(len(n))
    
    i += 1

    