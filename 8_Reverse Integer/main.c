#include <stdio.h>
#include <math.h>

int reverse(int x) {

    // it may happen the negation of a number to overflow, to prevent this, use long long
    long long number = x;

    int is_negative = 0;
    long long result = 0;

    if (x < 0) {
        is_negative = 1;
        number *= -1;
    }

    // get the number of digits of the number
    int number_length = (int) log10(number) + 1;

    // loop every digit (right to left)
    for (int i = 0; i < number_length; i++) {
        // extract the digit
        int extracted_digit = (int) number / (int) pow(10, i) % 10;

        result += (long long) (extracted_digit * (pow(10, (number_length - i - 1))));
    }

    // check if the number is not 32 bits
    if (result < -pow(2, 31) || result > pow(2, 31))
        return 0;

    return is_negative ? result * -1 : result;
}

int main() {

    int x = 0;

    int number = reverse(x);

    printf("%d\n", number);
    return 0;
}