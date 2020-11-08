class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:

        if len(nums) < 3:
            return []

        nums.sort()

        results = []

        for i in range(len(nums) - 2):

            j = i + 1
            k = len(nums) - 1

            while j < k:

                calc = nums[i] + nums[j] + nums[k]

                if calc == 0:

                    l = [nums[i], nums[j], nums[k]]
                    if l not in results:
                        results.append(l)

                    # lets try to find more
                    j += 1

                elif calc < 0:
                    j += 1
                elif calc > 0:
                    k -= 1

        return results


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))

nums = [-2, 0, 1, 1, 2]
print(Solution().threeSum(nums))

nums = [0]
print(Solution().threeSum(nums))
