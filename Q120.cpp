//https://leetcode.com/problems/triangle/?envType=daily-question&envId=2025-09-25
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& t) {
    
        for (int i = t.size() - 2; i >= 0; i--) {
            for (int j = 0; j < t[i].size(); j++) {
                
                t[i][j] += min(t[i+1][j], t[i+1][j+1]);
            }
        }
        return t[0][0]; 
    }
};
