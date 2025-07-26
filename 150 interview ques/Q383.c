/*https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150*/
#include <stdbool.h>

bool canConstruct(char* r, char* m) {
    int arr[26] = {};
    for(; *m;){
        int i = *(m) - 'a';
        arr[i] = arr[i] + 1;
        m++;
    }
    for(; *r ;){
        int i = *(r) - 'a';
        arr[i] = arr[i] - 1;
        if(arr[i] == -1){
            return false;
       
        }
        r++;
    

    }
    return true;


    
}