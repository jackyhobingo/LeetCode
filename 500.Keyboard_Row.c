/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool isInStr(char c, char *str, int lenStr) {
    for (int i = 0; i < lenStr; i++) {
        if (c == str[i]) {
            return true;
        }
    }
    return false;
}
 
char** findWords(char** words, int wordsSize, int* returnSize) {
    char query[3][30] = {
        "QWERTYUIOPqwertyuiop\0", "ASDFGHJKLasdfghjkl\0", "ZXCVBNMzxcvbnm\0"
    };

    char ** result = (char **)malloc(wordsSize * sizeof(char));
    *returnSize = 0;
    
    for (int i = 0; i < wordsSize; i++) {
        int n = strlen(words[i]);
        int j = 0;
        for (j = 0; j < 3 && !isInStr(words[i][0], query[j], strlen(query[j])); j++) {;}
        int k = 1;
        for (k = 1; k < n && isInStr(words[i][k], query[j], strlen(query[j])); k++) {;}
        if (k == n) {
            result[*returnSize] = (char *)malloc(sizeof(char) * (n + 1));
            result[(*returnSize) ++] = words[i];
        }
    }
    return result;
}
