"""
https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150"""
a = [1,2,3]
b = int("".join(map(str , a)))
c = b +1
d = [int(digit) for digit in str(c)]
print(d)

print(c)