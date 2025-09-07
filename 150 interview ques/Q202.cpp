//https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150
#include <vector>
using namespace std;
class Solution {
public:
    bool isHappy(int n) {
        while (n > 9 || n == 1) {
            vector<int> d;
            int temp = n;
            while (temp > 0) {
                d.push_back(temp % 10);
                temp /= 10;
            }
            
            int a = 0;
            for (int i = 0; i < d.size(); i++) {
                a += d[i] * d[i];
            }
            
            if (a == 1) {
                return true;
            }
            n = a;
        }
        if (n == 7) {
            return true;
        }
        return false;
    }
};