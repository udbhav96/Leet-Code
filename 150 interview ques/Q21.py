'''https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150'''

#Try 1 (37min)
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(m)):
    for j in range(i , len(m)):  
        m[i][j], m[j][i] = m[j][i], m[i][j] 

'''I had learn how to take the transpose of a matrix'''
#Try 2 (45min)
for i in m:
    n = len(i) 
    for j in range(n // 2):
    
        i[j], i[n - j - 1] = i[n - j - 1], i[j]
'''I had learn to flip the matrix (seen)'''

#Try 3 (Final)
class Solution(object):
    def rotate(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(m)):
            for j in range(i , len(m)):  
               m[i][j], m[j][i] = m[j][i], m[i][j] 

        for i in m:
           n = len(i) 
           for j in range(n // 2):
              i[j], i[n - j - 1] = i[n - j - 1], i[j]

