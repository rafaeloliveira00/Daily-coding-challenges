class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if len(s) == 0:
            return 0

        is_negative = False

        if s[0] == '-':
            is_negative = True
            s = s[1:]

        elif s[0] == '+':
            s = s[1:]

        elif not s[0].isdigit():
            return 0

        final = ''
        for c in s:
            if not c.isdigit():
                break
            final += c

        if final == '':
            return 0

        final_int = int(final)

        if is_negative:
            final_int *= -1

        if final_int < -2 ** 31:
            final_int = -2 ** 31

        if final_int >= 2 ** 31:
            final_int = (2 ** 31) - 1

        return final_int


my_str = '2147483648'
print(Solution().myAtoi(my_str))

my_str = '   -42'
print(Solution().myAtoi(my_str))

my_str = '4193 with words'
print(Solution().myAtoi(my_str))

my_str = 'words and 987'
print(Solution().myAtoi(my_str))

my_str = '-91283472332'
print(Solution().myAtoi(my_str))
