'''https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1 ( 45 min)
nums = [1,2,3,4]
answer = [0]*(len(nums))
i = 0 
a = 1
j = 0
b = 0
while i < len(nums):
   b = nums[i]
   nums[i] = 1
   while j < len(nums):
     a *= nums[j]
     j += 1
   answer[i] = a
   a = 1
   nums[i] = b
   j = 0
   i += 1
print(answer)
'''Error: This code is giving time complexity as i had define too many variable and reset them too many time , I think so ......But after an hr i found out i am fucked up  Check Try 2 for the blunder '''
#Try 2 (27min)
answer = [0]*(len(nums))
i = 0
j = 0
while i < len(nums):
    while j < len(nums):
     if i != j:
        answer[i] *= nums[j]
        j += 1
        i += 1
    print( answer)
'''Error : I am using while loop so i had to reset  the i and j so i change them to the for loop'''
#Try 3 (5 min)
n = len(nums) 
answer = [1]*(n)
for i in range(n):
    for j in range(n):
        if i != j:
             answer[i] *= nums[j]
print (answer)
'''Oki there is no error but giving time complexity for a particular case so i am now going to check the solution'''
#Try 4 - Final (25 min)
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        prevSuffix = 1
        for i in range(n - 2, -1, -1):
            prevSuffix *= nums[i + 1]
            ans[i] *= prevSuffix

        return ans
'''Its kinda a simple but my rotten brain can not think about it because of a lack of sleep i am going to sleep now '''