'''https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150'''
#Try 1(2hr 34min) 
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        i = 0
        j = 0 
        while i < len(citations) - 1:  
          j = i + 1
          while j < len(citations):  
           if citations[i] < citations[j]: 
            citations[i], citations[j] = citations[j], citations[i]  
           j += 1  
          i += 1  

        count = 0 
        b = 0 
        while b < len(citations):
          if citations[b] >= b + 1:
           count += 1
          b += 1
        return count

'''I learn the selection sorting alogorithm'''