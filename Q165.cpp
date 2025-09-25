//https://leetcode.com/problems/compare-version-numbers/description/
#include <string>
#include <unordered_map>
#include <cstdlib>
using namespace std;

class Solution {
public:
    static int compareVersion(string& ver1, string& ver2) {
         int num1=ver1.size(), num2=ver2.size();
        int x1=0, x2=0;
        for(int i=0, j=0; i<num1 || j<num2; i++, j++){
            while(i<num1 && ver1[i]!='.'){
                x1=10*x1+(ver1[i++]-'0');
            }
            while(j<num2 && ver2[j]!='.'){
                x2=10*x2+(ver2[j++]-'0');
            }
            if (x1<x2) return -1;
            else if (x1>x2) return 1;
            x1=0;
            x2=0;
        }
        return 0;
    }
};