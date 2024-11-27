"""
https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150
"""

a = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
c = 0
b = "VI"
for i in range(len(b)-1):
 if a[b[i]] < a[b[i + 1]]:
    c -= a[b[i]] 
 else :
    c += a[b[i]] 
print(c)
