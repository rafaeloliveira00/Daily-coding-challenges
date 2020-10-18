class Solution:
    brackets_matches = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    def isValid(self, s):
        s_list = list(s)

        # check if the number of elements in the list is even
        if len(s_list) % 2 != 0:
            return False

        # flag to control if the list suffered any changes while looping through the entire list
        changes = True

        while changes:
            changes = False
            for i, character in enumerate(s_list):

                # we will only compare a open bracket with a closing one
                # the following if statement will check if the current character is an open bracket, if not just ignore
                if character not in self.brackets_matches:
                    continue

                # check if the close bracket matches
                if self.brackets_matches[character] == s_list[i + 1]:
                    # if it matches remove both from the list, to remember when we delete an element, the list will
                    # shorten automatically, that's why the same position is been removed
                    del s_list[i]
                    del s_list[i]

                    changes = True

        # if the list is empty then everything was validated otherwise the string is invalid
        return True if not s_list else False


s = '()(){(())'
print(Solution().isValid(s))  # False

s = ''
print(Solution().isValid(s))  # True

s = '([{}])()'
print(Solution().isValid(s))  # True
