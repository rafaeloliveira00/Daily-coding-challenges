#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int myAtoi(char *s) {

    char final[50];
    int found_valid_numbers = 0;

    int is_negative = 0;
    // if true then we found a +, - or an number already
    int start_to_save = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == ' ') {
            if (start_to_save == 1)
                break;
        } else if (s[i] == '+') {
            if (start_to_save == 1)
                break;

            start_to_save = 1;
        } else if (s[i] == '-') {
            if (start_to_save == 1)
                break;

            start_to_save = 1;
            is_negative = 1;
        } else if (s[i] >= 48 && s[i] <= 57) {
            start_to_save = 1;

            // if it is an number, add it to the new string
            final[found_valid_numbers] = s[i];
            found_valid_numbers++;

        } else
            break;
    }

    // if the current position is 0, then we do not found a valid digit
    if (found_valid_numbers == 0)
        return 0;

    // convert the clean string to number
    int final_int = atoi(final);
    // convert to negative if has negative
    if (is_negative == 1)
        final_int *= -1;

    // cap the result
    if (final_int < -pow(2, 31))
        return (int) -pow(2, 31);

    else if (final_int >= pow(2, 31))
        return (int) pow(2, 31) - 1;

    return final_int;
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
