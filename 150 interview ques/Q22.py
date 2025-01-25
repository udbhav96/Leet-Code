'''https://leetcode.com/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1 (1hr 20 min)
'''This is to make row Zero'''
m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

for i in range(len(m)):
    row = m[i]
    if 0 in row:
        for j in range(len(row)):  
            m[i][j] = 0
        

print(m)
'''This is to make  coloums zero '''
for i in range(len(m)):
    row = m[i]
    for j in range(len(row)):
        if row[j] == 0:  
            for k in range(len(m)):
                m[k][j] = 0


print(m)
'''Error: I want to perform both the operation simultaneously but it got fucked up'''
#Try 2 (45min)
'''logic befind is that  i had to store the sindex  first then make it zero '''
class Solution(object):
    def setZeroes(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_rows = []
        zero_cols = []


        for i in range(len(m)):
           for j in range(len(m[i])):
             if m[i][j] == 0:
               if i not in zero_rows:
                zero_rows.append(i)

               if j not in zero_cols:
                zero_cols.append(j)  


        for i in zero_rows:
          for j in range(len(m[i])):
            m[i][j] = 0


        for j in zero_cols:
          for i in range(len(m)):
            m[i][j] = 0

        return m
'''It got submited but the space complexity is O(m*n)'''
#Try 3 ( 40 min)
'''Logic to make the space complexity to O(m+n)'''
m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]



zero_rows = []
zero_cols = []


for i in range(len(m)):
           for j in range(len(m[i])):
             if m[i][j] == 0:
               if i not in zero_rows:
                zero_rows.append(i)

               if j not in zero_cols:
                zero_cols.append(j)  

print(len(zero_rows))
print(len(zero_cols))
for i in zero_rows:
    for j in range(len(m[i])):
        m[i][j] = 0


for j in zero_cols:
    for i in range(len(m)):
        m[i][j] = 0

print(m)
#Try 4 (1hr 27 min)
'''Now to make complexity O(1)'''
def setZeroes(m):
    m_len = len(m)
    n_len = len(m[0])

    first_row_zero = False
    first_col_zero = False

    for j in range(n_len):
        if m[0][j] == 0:
            first_row_zero = True

    for i in range(m_len):
        if m[i][0] == 0:
            first_col_zero = True

    for i in range(1, m_len):
        for j in range(1, n_len):
            if m[i][j] == 0:
                m[i][0] = 0  
                m[0][j] = 0  

    for i in range(1, m_len):
        for j in range(1, n_len):
            if m[i][0] == 0 or m[0][j] == 0:
                m[i][j] = 0

    if first_row_zero:
        for j in range(n_len):
            m[0][j] = 0

    if first_col_zero:
        for i in range(m_len):
            m[i][0] = 0

m = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

setZeroes(m)
print(m)
'''Oki this question ends here '''


        