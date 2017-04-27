#include<limits.h>
int myAtoi(char* str) {
    int ans = 0;
    int sign = 1;
    // space
    while (*str == ' ') {
        str ++;
    }
    
    // sign
    if (*str == '+'){
        ++str;
    } else if (*str == '-'){
        sign = -1;
        ++str;
    }
    
    // digits
    for(int digit = *str - '0'; digit <= 9 && digit >= 0; digit = *(++str) - '0'){
        if (ans > INT_MAX / 10 || ans == INT_MAX / 10 && digit > INT_MAX % 10) {
            return sign > 0 ? INT_MAX : INT_MIN;
        }
        ans = 10 * ans + digit;
    }
    
    return ans * sign;
}