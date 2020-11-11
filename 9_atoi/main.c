#include <stdio.h>
#include <math.h>


int myAtoi(char *s) {

    long long final = 0;
    int is_negative = 0;
    // if true then we found a +, - or an number already
    int start_to_process = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == ' ') {
            if (start_to_process)
                break;
        } else if (s[i] == '+') {
            if (start_to_process)
                break;

            start_to_process = 1;
        } else if (s[i] == '-') {
            if (start_to_process)
                break;

            start_to_process = 1;
            is_negative = 1;
        } else if (s[i] >= 48 && s[i] <= 57) {
            start_to_process = 1;

            // multiplying by 10, will shift the digits to the left
            final = final * 10 + s[i] - '0';
            
            if (is_negative && final * -1 < -pow(2, 31))
                return (int) -pow(2, 31);

            else if (!is_negative && final >= pow(2, 31) - 1)
                return (int) pow(2, 31);

        } else
            break;
    }

    // convert to negative if has negative
    if (is_negative == 1)
        final *= -1;

    return (int) final;
}

int main(void) {
    char str[] = "  4193 with words";
    printf("%d\n", myAtoi(str));

    char str1[] = "     -42";
    printf("%d\n", myAtoi(str1));

    char str2[] = "4193 with words";
    printf("%d\n", myAtoi(str2));

    char str3[] = "words and 987";
    printf("%d\n", myAtoi(str3));

    char str4[] = "-91283472332";
    printf("%d\n", myAtoi(str4));
}
