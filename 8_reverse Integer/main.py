class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        if x > 0:
            x = str(x)[::-1]
            x = int(x)
        else:
            x = str(x)[1:][::-1]
            x = int(x) * -1

        if int.bit_length(x) > 31:
            return 0

        return x


x = -516
print(Solution().reverse(x))
