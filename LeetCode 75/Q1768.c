/*https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75*/
char* mergeAlternately(char* word1, char* word2) {
    int len1 = strlen(word1), len2 = strlen(word2);
    char* result = (char*) malloc(len1 + len2 + 1);

    int i = 0, j = 0, k = 0;

    for (; i < len1 && j < len2;) {
        result[k++] = word1[i++];
        result[k++] = word2[j++];
    }
    for (; i < len1;) {
        result[k++] = word1[i++];
    }
    for (; j < len2;) {
        result[k++] = word2[j++];
    }
    result[k] = '\0';
    return result;
}