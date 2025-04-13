'''https://leetcode.com/problems/3sum/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1 Kinda Seen [1.5 hr]
nums = [-1,0,1,2,-1,-4]
a = []
i = 0
while i < len(nums) - 1:  
    j = i + 1
    while j < len(nums):  
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        j += 1  
    i += 1
i = 0 
j = i + 1
k = len(nums)-1
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    j, k = i + 1, len(nums) - 1
    while j < k:
        d = nums[i] + nums[j] + nums[k]
        if d == 0:
            a.append([nums[i], nums[j], nums[k]])
            while j < k and nums[j] == nums[j + 1]:
                j += 1
            while j < k and nums[k] == nums[k - 1]:
                k -= 1
            j += 1
            k -= 1
        elif d < 0:
            j += 1
        else:
            k -= 1
print(a)
# Sort the input array
# Sorting helps in efficiently identifying triplets and handling duplicates.

# Iterate through the array
# Use a for loop to go through each element (nums[i]) as the first element of the triplet.

# Skip duplicates for the first element
# If the current element is the same as the previous one, skip this iteration to avoid duplicate triplets.

# Initialize two pointers for each iteration
# Set pointer j at the next element (i + 1) and pointer k at the last element of the array.

# Use the two-pointer technique to find triplets
# Calculate the sum of the current triplet: nums[i] + nums[j] + nums[k].

# If the sum is zero, we've found a valid triplet
# Add the triplet [nums[i], nums[j], nums[k]] to the result list.

# Skip duplicates for the second and third pointers (j and k)
# Move the left pointer (j) if nums[j] is the same as the previous element to avoid duplicates.
# Move the right pointer (k) if nums[k] is the same as the next element to avoid duplicates.

# Adjust the pointers to find other potential triplets
# If the sum is less than zero, increment the left pointer (j) to increase the sum.
# If the sum is greater than zero, decrement the right pointer (k) to decrease the sum.

# Return the result
# Once all possible triplets are checked, return the list of unique triplets.



    
    


