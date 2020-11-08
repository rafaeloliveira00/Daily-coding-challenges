class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:

        # we use the dictionary to store the complement and the index it was at
        complement = {}

        for i, num in enumerate(nums):
            if num in complement:
                return [complement[num], i]
            else:
                # add to the dictionary
                complement[target - num] = i

        return [-1, -1]


nums = [2, 7, 11, 15]
target = 9

print(Solution().twoSum(nums, target))

nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))

nums = [3, 3]
target = 6
print(Solution().twoSum(nums, target))
