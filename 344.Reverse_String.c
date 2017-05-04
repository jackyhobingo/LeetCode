char* reverseString(char* s) {
    int i;
    int n = strlen(s);
    char *temp = (char *)malloc(sizeof(char)*(n+1));
    for(i = 0; i < n; i++) {
        temp[i] = s[n-i-1];
    }
    temp[n] = '\0';
    return temp;
}
