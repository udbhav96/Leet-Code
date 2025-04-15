/*https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75*/
//Try 1( 30 min)
#include <stdbool.h>


bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
    int i = 0;
    int j = flowerbedSize - 1;
    int count = 0;
    
    while (i <= j) {
        if (flowerbed[i] == 1 || flowerbed[j] == 1) {
            i += 2;
            j -= 2;
            count += 1;
            flowerbed[i] = 1;
            flowerbed[j] = 1;
        } else {
            i += 1;
            j -= 1;
        }


    }
    count -= 1;

    if (count >= n) {
        return true;
        }

    return false;
}
//Error that i am blindingly putting flower = 1 not checking 
//Try 2 (Seen)

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
    int count = 0; 
    
    for (int i = 0; i < flowerbedSize; i++) {
        if (flowerbed[i] == 0 &&
            (i == 0 || flowerbed[i - 1] == 0) &&
            (i == flowerbedSize - 1 || flowerbed[i + 1] == 0)) { 
            flowerbed[i] = 1; 
            count++;  
            i++;  
        }
        
        if (count >= n) {
            return true;
        }
    }

    return false;
}
