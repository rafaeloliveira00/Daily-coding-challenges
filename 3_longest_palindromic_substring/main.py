class Solution:
    def longestPalindrome(self, s):

        max_palindrome = ''

        # loop through every character in the string
        for i in range(len(s)):
            # loop through every remaining character
            for j in range(i, len(s)):
                substring = s[i:j + 1]

                # check if the current substring is a palindrome and if is longest than the current palindrome
                if substring == substring[::-1] and len(max_palindrome) < len(substring):
                    max_palindrome = substring

        return max_palindrome


s = 'tracecars'
print(Solution().longestPalindrome(s))
