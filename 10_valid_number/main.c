#include <stdio.h>
#include "stdbool.h"

bool isDigit(char s) {
    return s >= '0' && s <= '9';
}

bool isNumber(char *s) {
    //states
    int NUMBER = 1, DOT = 2, E = 3, SIGN = 4, SPACE = 5;

    int current_state = 0;

    bool got_dot = false, got_e = false, got_numbers = false;

    for (int i = 0; s[i] != '\0'; i++) {
        // if the current state is 0 then we just started or only found white spaces so far
        if (s[i] == ' ') {
            if (current_state == 1) {
                current_state = SPACE;
                continue;
            } else
                continue;
        }

        // initial state
        if (current_state == 0) {
            // check if we got a number
            if (isDigit(s[i])) {
                current_state = NUMBER;
                got_numbers = true;
                continue;
            } else if (s[i] == '.') {
                current_state = DOT;
                got_dot = true;
                continue;
            } else if (s[i] == '+' || s[i] == '-') {
                current_state = SIGN;
                continue;
            } else
                return false;
        }
            // if the state is NUMBER
        else if (current_state == NUMBER) {
            if (isDigit(s[i])) {
                got_numbers = true;
                continue;
            } else if (s[i] == '.' && !got_dot) {
                current_state = DOT;
                got_e = true;
                continue;
            } else if (s[i] == 'e' && !got_e) {
                current_state = E;
                got_e = true;
                continue;
            } else
                return false;
        }
            // if the state is DOT
        else if (current_state == DOT) {
            if (isDigit(s[i])) {
                got_numbers = true;
                current_state = NUMBER;
                continue;
            } else if (s[i] == 'e' && got_numbers) {
                got_e = true;
                current_state = E;
                continue;
            } else
                return false;
        }
            // if the state is E
        else if (current_state == E) {
            // can not have any more dots so, lets lie and say that we found a dot
            got_dot = true;
            if (isDigit(s[i])) {
                got_numbers = true;
                current_state = NUMBER;
                continue;
            } else if (s[i] == '+' || s[i] == '-') {
                current_state = SIGN;
                continue;
            } else
                return false;
        }
            // if the state is SIGN
        else if (current_state == SIGN) {
            if (isDigit(s[i])) {
                got_numbers = true;
                current_state = NUMBER;
                continue;
            } else if (s[i] == '.' && !got_dot) {
                current_state = DOT;
                got_dot = true;
                continue;
            } else
                return false;
        }
            // if the state is SPACE
        else if (current_state == SPACE) {
            if (s[i] != ' ')
                return false;
        }
    }

    if (current_state != SPACE && current_state != NUMBER && current_state != DOT || !got_numbers)
        return false;

    return true;
}

int main() {
    printf("%d", isNumber(". 9"));
    return 0;
}
