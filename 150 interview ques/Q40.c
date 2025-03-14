/*https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150*/
//Try 1 (20 min)
#include <stdbool.h>

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    for (int i = 0; i < matrixSize; i++) {
        int left = 0;
        int right = matrixColSize[i] - 1;  // Corrected initialization of right

        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (matrix[i][mid] == target) {
                return true;
            }
            if (matrix[i][mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    return false;
}
