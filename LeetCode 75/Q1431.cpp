//https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1765913897/?envType=study-plan-v2&envId=leetcode-75
#include <vector>
using namespace std;
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& c, int extraCandies) {
        vector<bool> ci(c.size());
        int a = c[0];
        for(int i = 0 ; i < c.size()  ; i++){
            if(c[i] > a){
                a = c[i];
            }
        }
        for(int i = 0 ; i < c.size() ; i ++){
            if(a > (c[i] + extraCandies)){
                ci[i] = false;
            }
            else{
                ci[i] = true;
            }
        
        }
        return ci;

    }
};