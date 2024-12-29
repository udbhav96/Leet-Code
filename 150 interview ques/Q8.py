"""
https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
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
        for i in range(len(s)-1):
           if a[s[i]] < a[s[i+1]]:
             c -= a[s[i]] 
           else :
             c += a[s[i]] 
        c += a[s[-1]]

        return c

'''Concept: Hash Table :-A hash table is a data structure that stores key-value pairs.
It uses a hash function to compute an index into an array of buckets or slots,
where the desired value can be found.

In Python, hash tables are implemented as dictionaries (dict).
 Dictionaries provide average O(1) time complexity for lookups, insertions, and deletions'''

'''New Feature: I can use one index to access another, like a[b[0]], 
where the index from 'b' is used to access an element in 'a'.
'''