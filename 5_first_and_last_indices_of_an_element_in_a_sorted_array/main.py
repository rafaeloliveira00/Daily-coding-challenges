class Solution:
    def getRange(self, arr, target):

        result = [-1, -1]

        for i, value in enumerate(arr):
            if value == target:
                # set the first occurrence
                if result[0] == -1:
                    result[0] = i

                # update the last index
                result[1] = i

        return result


arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 9]
x = 2
print(Solution().getRange(arr, x))
