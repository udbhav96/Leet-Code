'''https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1 (20 min)
a = [2,7,11,15]
t = 9 
i = 0
b = [ 0 , 0]
while i < len(a):
    j = i + 1 
    while j < len(a):
        if a[i] + a[j] == t :
            b[0] = i + 1
            b[1] = j + 1
        j += 1
    i += 1
print(b)
'''Code is giving out but getting time limit exeeded in the particulat case'''
#Try 2 (Seen) Optimize Code
class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while r > l:
            if numbers[r] + numbers[l] == target:
                return [l + 1, r + 1]
            elif numbers[r] + numbers[l] > target:
                r -= 1
            else:
                l += 1
        return [-1, -1]