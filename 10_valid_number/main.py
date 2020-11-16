class Solution:
    def isNumber(self, s: str) -> bool:
        # this problem was solved by using a finite state machine

        # states
        NUMBER = 1
        DOT = 2
        E = 3
        SIGN = 4

        current_state = 0

        got_dot = False
        got_e = False
        got_numbers = False

        s = s.strip()

        for c in s:
            # first iteration
            if current_state == 0:
                if c.isdigit():
                    current_state = NUMBER
                    got_numbers = True
                    continue
                elif c == '.':
                    current_state = DOT
                    got_dot = True
                    continue
                elif c == '+' or c == '-':
                    current_state = SIGN
                    continue
                else:
                    return False

            if current_state == NUMBER:
                if c.isdigit():
                    got_numbers = True
                    continue
                elif c == '.' and got_dot is False:
                    current_state = DOT
                    got_dot = True
                    continue
                elif c == 'e' and got_e is False:
                    current_state = E
                    got_e = True
                    continue
                else:
                    return False
            elif current_state == DOT:
                if c.isdigit():
                    got_numbers = True
                    current_state = NUMBER
                    continue
                elif c == 'e' and got_numbers is True:
                    got_e = True
                    current_state = E
                    continue
                else:
                    return False
            elif current_state == E:
                # can not have a decimal value after the e
                got_dot = True
                if c.isdigit():
                    got_numbers = True
                    current_state = NUMBER
                    continue
                elif c == '+' or c == '-':
                    current_state = SIGN
                    continue
                else:
                    return False
            elif current_state == SIGN:
                if c.isdigit():
                    got_numbers = True
                    current_state = NUMBER
                    continue
                elif c == '.' and got_dot is False:
                    current_state = DOT
                    got_dot = True
                    continue
                else:
                    return False

        # if the last state is not the state NUMBER or the DOT then return false
        if current_state != NUMBER and current_state != DOT or got_numbers is False:
            return False

        return True


num = '.1e21 '
print(Solution().isNumber(num))  # True

num = '0.1'
print(Solution().isNumber(num))  # True

num = '1abc1'
print(Solution().isNumber(num))  # False

num = '2e10'
print(Solution().isNumber(num))  # True

num = '6e-1'
print(Solution().isNumber(num))  # True

num = '99e2.5'
print(Solution().isNumber(num))  # False
