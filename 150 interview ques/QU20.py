'''https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1
'''Step 1 [Finding the total number of element in the matrix]'''
m = [[1,2,3],[4,5,6],[7,8,9]]

b = 0
for i in range (len(m)):
    for j in range (len(m[i])):   
        b += 1
print(b)    
'''Step 2 [Print all the element in the matrix in a blank list a]'''
a = [0]*b
c = 0
k = 0
for i in range (len(m)):
    for j in range (len(m[i])):       
            c = m[i][j]
            a[k]  = c   
            k += 1  
        
print(a)  