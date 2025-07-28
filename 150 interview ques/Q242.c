/*https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150*/
//Try 1 
#include <stdbool.h>
#include <stdio.h>
bool isAnagram(char* s, char* t) {
    int i  = 0;
    int j = 0 ;
    while(s[i] != '\0'){
        i++;

    }
    while(t[j] != '\0'){
        j++;
    }
    if(i != j){
        return false;
    }
    int arr[i];  // Valid VLA
    for (int n = 0; n < i; n++) {
    arr[n] = 0;
}
    
    for(int l = 0 ; l < i ; l++){
        int k = 0 ;
        while(t[k] != '\0'){
            if(s[l] == t[k] ){
                arr[l] = 1 ;
                for( int f = k ; f < j - 1 ; f++) {
                    t[f] = t[f+1];
                }
                j--;
                break ;
                
            }
            k++;
        }
    }
    for(int y = 0 ; y < i  ; y++){
        if( arr[y] == 0  && t[0] != '\0'){
            return false;
        }
    }
    if(t[0] == '\0'){
        return true;
    }
    return true;

    
}
// I am dumb fr 
//Try 2 
bool isAnagram(const char *s, const char *t) {
    if (strlen(s) != strlen(t)) return false;

    int count[26] = {0};

    for (int i = 0; s[i]; i++) {
        count[s[i] - 'a']++;
        count[t[i] - 'a']--;
    }

    for (int i = 0; i < 26; i++) {
        if (count[i] != 0) return false;
    }

    return true;
}

