"""
https://leetcode.com/problems/reverse-bits/?envType=study-plan-v2&envId=top-interview-150
"""
a = input("enter a binary number ")
d = list(map(int, str(a)))
print(d)
i = 0
for i in range(len(d) // 2):
     d[i], d[-(i + 1)] = d[-(i + 1)], d[i]
a = ''.join(map(str, d))


decimal_number = int(a, 32)
print(decimal_number)
