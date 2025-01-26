'''https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150'''
#Try 5 [1.4hr ](final)
class Solution(object):
    def intToRoman(self, d):
        """
        :type num: int
        :rtype: str
        """
        a = { 
            1 : "I",
            4 : "IV",
            5 : "V",
            9 : "IX",
            10: "X",
            40: "XL",
            50: "L", 
            90: "XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }


        c = list(str(d))
        e = [0]*len(c)
        k =""
        for i in range(len(c)):
           e[i]= int(c[i]) * 10**(len(c)-i-1)
        for i in range (len(e)):
          if e[i] == 0:
           continue
          if e[i] in a:
           k += a[e[i]]
          else:
            if int(c[i]) > 5:
              k += a[5 * 10**(len(c) - i - 1)]  
              e[i] -= 5 * 10**(len(c) - i - 1)  

              while e[i] >= 1:
                k += a[1 * 10**(len(c) - i - 1)] 
                e[i] -= 1 * 10**(len(c) - i - 1)  
            else:
              while e[i] >= 1:
                k += a[1 * 10**(len(c) - i - 1)]  
                e[i] -= 1 * 10**(len(c) - i - 1)  

        return k




'''It kinda hard i forgot to save my tries'''