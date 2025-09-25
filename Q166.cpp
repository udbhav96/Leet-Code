//https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#include <string>
#include <unordered_map>
#include <cstdlib>
using namespace std;

class Solution {
public:
    string fractionToDecimal(int n, int d) {
        if (n == 0) {
            return "0";
        }

        string r = "";
        if (n < 0 ^ d < 0) {
            r += "-";
        }

        long long di = std::llabs((long long)n);
        long long dv = std::llabs((long long)d);

        r += std::to_string(di / dv);
        long long re = di % dv;
        if (re == 0) {
            return r;
        }

        r += ".";
        std::unordered_map<long long, int> map;

        while (re != 0) {
            if (map.count(re)) {
                r.insert(map[re], "(");
                r += ")";
                return r;  
            }
            map[re] = r.size();
            re *= 10;
            r += std::to_string(re / dv);
            re = re % dv;
        }

        return r; 
    }
};
//good question for newbie to undertand types

