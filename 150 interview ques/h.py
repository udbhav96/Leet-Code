num = [4,5,6,1,2,3]
for i in range(len(num)-1):
    if(num[i] > num[i+1]):
        break
print(i)