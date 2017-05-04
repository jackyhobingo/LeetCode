/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** fizzBuzz(int n, int* returnSize) {
    char ** result = (char**)malloc(sizeof(char *) * n);
    int i;
    int upper = 10;
    int digit_size = 2;
    for (i = 1; i <= n; i++) {
        if (i % 15 == 0) {
            result[i - 1] = (char *)malloc(sizeof(char) * 9);
            sprintf(result[i - 1], "FizzBuzz");
        } else if (i % 3 == 0) {
            result[i - 1] = (char *)malloc(sizeof(char) * 5);
            sprintf(result[i - 1], "Fizz");
        } else if (i % 5 == 0) {
            result[i - 1] = (char *)malloc(sizeof(char) * 5);
            sprintf(result[i - 1], "Buzz");
        } else {
            if (i >= upper) {
                upper *= 10;
                digit_size ++;
            }
            result[i - 1] = (char *)malloc(sizeof(char) * digit_size);
            sprintf(result[i - 1], "%d", i);
        }
    }
    *returnSize = n;
    return result;
}
