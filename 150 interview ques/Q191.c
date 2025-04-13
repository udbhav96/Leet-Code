/*https://leetcode.com/problems/number-of-1-bits/?envType=study-plan-v2&envId=top-interview-150*/
//Try 1 ( 30 min)
int hammingWeight(int n) {
    int count = 0;
    while(n != 0){
        if (n % 2 == 0) {
            n = n/2;
            
        } else {
            n = n -1;
            count = count + 1 ;
        }  
    }
    return count ;
    
}
//easy pesy
