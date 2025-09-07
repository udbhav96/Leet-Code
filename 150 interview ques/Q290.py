'''https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150'''
class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()  
        if len(pattern) != len(words):  
            return False
        
        c_t_w = {}  
        w_t_c = {}  
        
        for i in range(len(pattern)):
            c = pattern[i]
            w = words[i]
            
            if c in c_t_w:
                if c_t_w[c] != w:
                    return False
            if w in w_t_c:
                if w_t_c[w] != c:
                    return False
            
            c_t_w[c] = w
            w_t_c[w] = c
        
        return True
