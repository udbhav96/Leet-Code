'''https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150'''
#try 1
a = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
b = 1
for i in range (len(a)):
    for j in range (len(a)):
        a[i][j] = b 
        b += 1
        j += 1
        
            
i += 1
print(a)
'''Just learened how to map the matrix'''

#try 2
a= [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
for i in range(len(a)):
    for j in range(len(a)):
         for k in  range ( j+1 , len(a)):
              if a[i][j] == a[i][k] and a[i][j] != '.':
                   print("False")

'''Check Coloum condition only'''
 #try 3 
for e in range(len(a)):
    for j in range(0,3,3):  
        for i in range(0,3,3):
            if a[i][j] == '.':
                continue
            for k in range(i + 1, len(a)):
                if a[i][j] == a[k][j]:
                    print(f"Duplicate found in column: {a[i][j]} at positions {i} and {k}")
                    d = False
a = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]

 
'''This particular piece of the code is to full fill  the third  3 x 3 grid condition'''
#try 4
def check_duplicates(board):
    d = True  
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                continue
            for k in range(j + 1, len(board[i])):
                if board[i][j] == board[i][k]:
                    print(f"Duplicate found in row: {board[i][j]} at positions {j} and {k}")
                    d = False  

    
    for j in range(len(board[0])):  
        for i in range(len(board)):
            if board[i][j] == '.':
                continue
            for k in range(i + 1, len(board)):
                if board[i][j] == board[k][j]:
                    print(f"Duplicate found in column: {board[i][j]} at positions {i} and {k}")
                    d = False  
    for e in range (len(board)):
      for j in range(0,3,3):  
        for i in range(0,3,3):
            if board[i][j] == '.':
                continue
            for k in range(i + 1, len(board)):
                if board[i][j] == board[k][j]:
                    print(f"Duplicate found in column: {board[i][j]} at positions {i} and {k}")
                    d = False     
      for i in range(0,3,3):  
        for j in range(0,3,3):
            if board[i][j] == '.':
                continue
            for k in range(j + 1, len(board)):
                if board[i][j] == board[k][j]:
                    print(f"Duplicate found in column: {board[i][j]} at positions {i} and {k}")
                    d = False
    e += 1
    return d  
board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]

result = check_duplicates(board)


print(result) 
'''This particular code is working on all  3 condition but some cases are not  working '''
#try 5 (5 hr , Final)
class Solution(object):
    def isValidSudoku(self, board):
        d = True
        for i in range(len(board)):
          for j in range(len(board[i])):
            if board[i][j] == '.':
                continue  
            for k in range(j + 1, len(board[i])):
                if board[i][j] == board[i][k]:
                    d = False

        for j in range(len(board[0])):
          for i in range(len(board)):
            if board[i][j] == '.':
                continue  
            for k in range(i + 1, len(board)):
                if board[i][j] == board[k][j]:
                    d =  False

        for box_row in range(0, 9, 3):  
          for box_col in range(0, 9, 3):  
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == '.':
                        continue
                    for m in range(box_row, box_row + 3):
                        for n in range(box_col, box_col + 3):
                            if (i != m or j != n) and board[i][j] == board[m][n]:
                                d = False

        return d  

             
           
        
              
        
