//https://leetcode.com/problems/count-elements-with-maximum-frequency/description/
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        int freq[101] = {0};   
        int maxFreq = 0, res = 0;

        for (int n : nums) {
            int f = ++freq[n];  
            if (f > maxFreq) {
                maxFreq = f;
                res = f;
            } else if (f == maxFreq) {
                res += f;
            }
        }

        return res;
    }
};