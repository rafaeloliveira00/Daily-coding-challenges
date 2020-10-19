class Solution:
    def lengthOfLongestSubstring(self, s):

        # variable that will contain the longest number
        longest_number = 0

        # temporary count value
        tmp = 0

        # temporary list that will contain the temporary characters
        chars_list = []

        # loop char by char
        for i, c in enumerate(s):
            if c not in chars_list:
                chars_list.append(c)
                tmp += 1

                if tmp >= longest_number:
                    longest_number = tmp
            else:
                # we found a similar
                if tmp >= longest_number:
                    longest_number = tmp

                chars_list.clear()

                # include the current character
                tmp = 1
                chars_list.append(c)

                # backpropagation, it is used to fetch some non-repetitive characters that may be in the back
                for j in range(i - 1, 0, -1):
                    back_character = s[j]
                    if back_character != c:
                        tmp += 1
                        chars_list.append(back_character)
                    else:
                        break

        return longest_number


print(Solution().lengthOfLongestSubstring('abcabcbb'))
