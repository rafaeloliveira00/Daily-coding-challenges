class Solution:
    def lengthOfLongestSubstring(self, s):

        # variable that will contain the longest number
        longest_number = 0

        # temporary count value
        tmp = 0

        # temporary list that will contain the temporary characters
        chars_list = []

        # loop char by char
        for c in s:
            if c not in chars_list:
                chars_list.append(c)
                tmp += 1
            else:
                # we found a similar
                if tmp >= longest_number:
                    longest_number = tmp
                    print(chars_list)

                chars_list.clear()

                # include the current character
                tmp = 1
                chars_list.append(c)

        return longest_number


print(Solution().lengthOfLongestSubstring('abrkaabcdaefghijjxxx'))
