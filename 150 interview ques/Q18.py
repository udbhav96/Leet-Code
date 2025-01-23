'''https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150'''
a = [1 , 3 , 1]
i = 0
j = 0 
while i < len(a) - 1:  
    j = i + 1
    while j < len(a):  
        if a[i]  < a[j]: 
            a[i], a[j] = a[j], a[i]  
        j += 1  
    i += 1  
print(a)
count = 0 
b = 0
while b < len(a):
    if a[b] >= b + 1:
        count += 1
    b += 1
print(count)