'''https://leetcode.com/problems/game-of-life/?envType=study-plan-v2&envId=top-interview-150'''
#I forgot the save trials
#Try 1 ( Put horizontal and vertical neigbours in one list)
#Try 2 ( Put horizontal ones and refine the code)
#Try 3 Final(2hr 30 min )
b = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
l = [g[:] for g in b]

i = 0 
while i < len(b)  :
    j = 0 
    while j < len(b[i]) :
        a = []
        c = 0
        if i -1 >= 0:
            a.append(b[i-1][j])
        if j -1 >= 0:
            a.append(b[i][j-1])
        if i + 1 < len(b):
            a.append(b[i+1][j])
        if j + 1 < len(b[i]):
            a.append(b[i][j+1])
        if i - 1 >= 0 and j -1 >= 0:
            a.append(b[i-1][j-1]) 
        if i - 1 >= 0 and j + 1 < len(b[i]):
            a.append(b[i-1][j+1])
        if i + 1 < len(b) and j -1 >= 0:
            a.append(b[i+1][j-1]) 
        if i + 1 < len(b) and j + 1 < len(b[i]):
            a.append(b[i+1][j+1])
        for k in a:
            if k == 1:
                c += 1
        if l[i][j] == 0:
            if c == 3:
                l[i][j] = 1
        elif l[i][j] == 1 :
            if c < 2 or c > 3:
                l[i][j] = 0
        j += 1
    i += 1
print(l)     
'''Good code but too many if's not the well structure code'''
#Optimum code( will see it later)