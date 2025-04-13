'''https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150'''
#Try 5 (Seen)(1 hr 30 min)
m = [[1,2,3],[4,5,6],[7,8,9]]
c = []
top = 0
left = 0
bottom = len(m) - 1
right  = len(m[0]) - 1
while top <= bottom and left <= right:
    for i in range(top , right+1):
        c.append(m[top][i])
    top += 1
    for i in range(top , bottom+1):
        c.append(m[i][bottom])
    right -= 1
    if top <= bottom:
        for i in range(right , left - 1 , -1):
            c.append(m[bottom][i])
        bottom -= 1
    if left <= right:
        for i in range(bottom , top -1 , -1):
            c.append(m[i][left])
    
print(c)
'''sorry i attemted this question several time but in the end i had to see its solution this is the optimum code'''

# The code performs a spiral traversal of a 2D matrix.
# It maintains four boundaries: top, bottom, left, and right.
# In each loop iteration, it:
#   1. Traverses the top row from the current left boundary to the right.
#   2. Traverses the rightmost column from the updated top to the bottom.
#   3. If rows remain, traverses the bottom row from the right boundary back to the left.
#   4. If columns remain, traverses the leftmost column upward from the bottom.
# After each pass, it adjusts the boundaries inward.
# This continues until all elements are visited, resulting in a spiral order collection.




